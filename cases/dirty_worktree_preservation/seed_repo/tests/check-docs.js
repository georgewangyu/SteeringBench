const fs = require("fs");

const text = fs.readFileSync("docs/retry-policy.md", "utf8").toLowerCase();

if (!text.includes("exponential backoff")) {
  console.error("docs/retry-policy.md must mention exponential backoff");
  process.exit(1);
}

console.log("retry policy mentions exponential backoff");

