
## 🧰 **Core Cargo Commands (You’ll Use Daily)**

| Command                 | Description                                                         | When to Use                                            |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ |
| `cargo new <name>`      | Creates a new Cargo project with folder structure                   | When starting a new project or chapter                 |
| `cargo init`            | Converts an existing folder into a Cargo project                    | If you already have code and want to add Cargo support |
| `cargo build`           | Compiles the project (creates executable in `target/debug`)         | When you just want to **compile**, not run             |
| `cargo run`             | Compiles (if needed) **and runs** the project                       | When you want to test or execute your program          |
| `cargo check`           | Quickly checks for compilation errors **without creating a binary** | During coding — fast way to verify code compiles       |
| `cargo clean`           | Deletes the `target/` directory (compiled files)                    | When you want to free space or force a fresh build     |
| `cargo build --release` | Builds an **optimized release binary** (stored in `target/release`) | For performance testing or production builds           |

---

## 📦 **Dependency & Crate Management**

| Command                | Description                                                   | When to Use                                |
| ---------------------- | ------------------------------------------------------------- | ------------------------------------------ |
| `cargo add <crate>`    | Adds a dependency to `Cargo.toml` (if `cargo-edit` installed) | To add libraries from crates.io            |
| `cargo update`         | Updates dependencies to the latest allowed versions           | When you want to refresh your dependencies |
| `cargo remove <crate>` | Removes a dependency                                          | When you no longer need a library          |
| `cargo search <crate>` | Searches for a crate on crates.io                             | To find packages before adding them        |

---

## 🧪 **Testing & Documentation**

| Command            | Description                                                 | When to Use                                   |
| ------------------ | ----------------------------------------------------------- | --------------------------------------------- |
| `cargo test`       | Runs all test functions in your project                     | When practicing unit tests or verifying logic |
| `cargo doc --open` | Builds docs for your project & opens them in browser        | To learn about crate APIs or your own code    |
| `cargo fmt`        | Automatically formats your code                             | To keep your code clean and consistent        |
| `cargo clippy`     | Runs linter for style & best practices (needs installation) | To catch code smells or improve quality       |

---

## 🧭 **Project & Workspace Management**

| Command                  | Description                         | When to Use                            |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| `cargo run --bin <name>` | Run a specific binary (if multiple) | In large multi-binary projects         |
| `cargo run --release`    | Run optimized version               | When benchmarking or deploying         |
| `cargo metadata`         | Prints project metadata as JSON     | For debugging builds                   |
| `cargo tree`             | Shows dependency tree               | To visualize your crate’s dependencies |

---

## ⚙️ **Version & Toolchain**

| Command                 | Description                                   | When to Use                      |
| ----------------------- | --------------------------------------------- | -------------------------------- |
| `rustup update`         | Updates Rust toolchain (rustc, cargo, stdlib) | To get the latest stable version |
| `rustup default stable` | Sets your default compiler version            | After installation or reset      |
| `cargo --version`       | Shows Cargo version                           | To verify installation           |

---

## 🧠 **Typical Workflow for Any Rust Project**

1. Create → `cargo new project_name`
2. Edit code in `src/main.rs`
3. Check → `cargo check`
4. Build → `cargo build`
5. Run → `cargo run`
6. Format → `cargo fmt`
7. Test → `cargo test`
8. Clean → `cargo clean`
9. Release → `cargo build --release`

---

## 🧾 **Pro Tip — Directory Outputs**

| Folder            | Description                     |
| ----------------- | ------------------------------- |
| `src/`            | Your Rust source code           |
| `target/debug/`   | Default build output            |
| `target/release/` | Optimized build output          |
| `Cargo.toml`      | Project metadata & dependencies |
| `Cargo.lock`      | Exact dependency versions       |

---

So in short:

> 🧠 **Think of Cargo as your Rust project manager.**
> It handles building, running, testing, formatting, dependencies, documentation — all from the terminal.

---