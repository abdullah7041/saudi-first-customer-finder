#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAME = "finding-first-customers";

// Build artefacts that must never reach an installed skill directory.
const SKIP_ENTRIES = new Set(["__pycache__", ".DS_Store", "node_modules", "outputs", ".npmignore"]);
const SKIP_EXTENSIONS = new Set([".pyc", ".pyo", ".log"]);

const TARGETS = {
  claude: () => path.join(os.homedir(), ".claude", "skills"),
  codex: () => path.join(process.env.CODEX_HOME || path.join(os.homedir(), ".codex"), "skills"),
  agents: () => path.join(os.homedir(), ".agents", "skills"),
};

function usage() {
  console.log(`
Finding First Customers — skill installer

Usage:
  node scripts/install.js                        # ~/.claude/skills
  node scripts/install.js --agent codex          # ~/.codex/skills
  node scripts/install.js --agent both
  node scripts/install.js --skills-dir ./.claude/skills
  node scripts/install.js --link                 # symlink instead of copy (dev)

Options:
  --agent NAME       claude (default) | codex | agents | both
  --skills-dir PATH  Install into a specific skills directory (overrides --agent)
  --link             Link to this checkout instead of copying, so edits apply live
  --help             Show this help

  agent = ~/.agents/skills, the cross-runtime directory Codex, Copilot CLI and
  Gemini CLI also read. "both" means claude + codex.
`);
}

function expandHome(value) {
  if (!value) return value;
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function parseArgs(argv) {
  const options = { agent: "claude" };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--help" || arg === "-h") {
      options.help = true;
      continue;
    }
    if (arg === "--link") {
      options.link = true;
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
      if (!["codex", "claude", "agents", "both"].includes(value)) {
        throw new Error(`Unknown agent: ${value}. Use claude, codex, agents, or both.`);
      }
      options.agent = value;
      index += 1;
      continue;
    }
    throw new Error(`Unknown option: ${arg}`);
  }
  return options;
}

function skipped(entry) {
  return SKIP_ENTRIES.has(entry.name) || SKIP_EXTENSIONS.has(path.extname(entry.name));
}

function copyDirectory(source, destination) {
  fs.mkdirSync(destination, { recursive: true });
  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    if (skipped(entry)) continue;
    const sourcePath = path.join(source, entry.name);
    const destinationPath = path.join(destination, entry.name);
    if (entry.isDirectory()) copyDirectory(sourcePath, destinationPath);
    else if (entry.isFile()) fs.copyFileSync(sourcePath, destinationPath);
  }
}

// Removes a previous install whether it is a real directory or a symlink/junction.
function removeExisting(target) {
  let stats;
  try {
    stats = fs.lstatSync(target);
  } catch {
    return;
  }
  if (stats.isSymbolicLink() || stats.isFile()) fs.unlinkSync(target);
  else fs.rmSync(target, { recursive: true, force: true });
}

function verify(destination) {
  const skillFile = path.join(destination, "SKILL.md");
  if (!fs.existsSync(skillFile)) throw new Error(`Install incomplete: missing ${skillFile}`);
  const text = fs.readFileSync(skillFile, "utf8");
  const match = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text);
  if (!match) throw new Error(`Install incomplete: ${skillFile} has no YAML frontmatter`);
  if (!/^name:\s*\S/m.test(match[1]) || !/^description:\s*\S/m.test(match[1])) {
    throw new Error(`Install incomplete: ${skillFile} frontmatter needs name and description`);
  }
}

function installTo(source, skillsDir, options) {
  const resolved = path.resolve(skillsDir);
  const destination = path.join(resolved, SKILL_NAME);
  fs.mkdirSync(resolved, { recursive: true });
  removeExisting(destination);

  if (options.link) {
    // "junction" is the only directory link Windows grants without elevation;
    // it is ignored on POSIX, where symlinkSync makes a normal symlink.
    fs.symlinkSync(source, destination, "junction");
    console.log(`Linked: ${destination} -> ${source}`);
  } else {
    copyDirectory(source, destination);
    console.log(`Installed: ${destination}`);
  }

  verify(destination);
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
      ? [TARGETS.claude(), TARGETS.codex()]
      : [TARGETS[options.agent]()];

  for (const directory of directories) installTo(source, directory, options);

  console.log("");
  console.log("The skill is not loaded until the agent restarts. Restart it, then run:");
  console.log(`  Use $${SKILL_NAME} in deep mode to find potential first customers for https://example.com`);
}

try {
  main();
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
