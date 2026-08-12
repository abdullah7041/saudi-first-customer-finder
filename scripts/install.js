#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAME = "saudi-first-customer-finder";

const TARGETS = {
  codex: () => path.join(process.env.CODEX_HOME || path.join(os.homedir(), ".codex"), "skills"),
  claude: () => path.join(os.homedir(), ".claude", "skills"),
};

function usage() {
  console.log(`
Saudi First Customer Finder — skill installer

Usage:
  npx saudi-first-customer-finder-skill
  npx saudi-first-customer-finder-skill --agent claude
  npx saudi-first-customer-finder-skill --skills-dir ./.claude/skills

Options:
  --agent NAME       codex (default) | claude | both
  --skills-dir PATH  Install into a specific skills directory (overrides --agent)
  --help             Show this help
`);
}

function expandHome(value) {
  if (!value) return value;
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function parseArgs(argv) {
  const options = { agent: "codex" };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--help" || arg === "-h") {
      options.help = true;
      continue;
    }
    if (arg === "--skills-dir") {
      const value = argv[index + 1];
      if (!value) throw new Error("--skills-dir requires a value");
      options.skillsDir = expandHome(value);
      index += 1;
      continue;
    }
    if (arg === "--agent") {
      const value = argv[index + 1];
      if (!value) throw new Error("--agent requires a value");
      if (!["codex", "claude", "both"].includes(value)) {
        throw new Error(`Unknown agent: ${value}. Use codex, claude, or both.`);
      }
      options.agent = value;
      index += 1;
      continue;
    }
    throw new Error(`Unknown option: ${arg}`);
  }
  return options;
}

function copyDirectory(source, destination) {
  fs.mkdirSync(destination, { recursive: true });
  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    const sourcePath = path.join(source, entry.name);
    const destinationPath = path.join(destination, entry.name);
    if (entry.isDirectory()) copyDirectory(sourcePath, destinationPath);
    else if (entry.isFile()) fs.copyFileSync(sourcePath, destinationPath);
  }
}

function installTo(source, skillsDir) {
  const resolved = path.resolve(skillsDir);
  const destination = path.join(resolved, SKILL_NAME);
  fs.mkdirSync(resolved, { recursive: true });
  fs.rmSync(destination, { recursive: true, force: true });
  copyDirectory(source, destination);
  console.log(`Installed: ${destination}`);
  return destination;
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    usage();
    return;
  }

  const source = path.resolve(__dirname, "..", SKILL_NAME);
  if (!fs.existsSync(source)) throw new Error(`Cannot find bundled skill at ${source}`);

  const directories = options.skillsDir
    ? [options.skillsDir]
    : options.agent === "both"
      ? [TARGETS.codex(), TARGETS.claude()]
      : [TARGETS[options.agent]()];

  for (const directory of directories) installTo(source, directory);

  console.log("");
  console.log("Restart your agent, then run:");
  console.log(`  Use $${SKILL_NAME} in deep mode to find potential first customers in Saudi Arabia for https://example.com`);
}

try {
  main();
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
