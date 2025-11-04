## 🧩 Core Idea

| Feature              | `mut` (Mutable variable)              | **Shadowing** (`let x = ...` again)                              |
| -------------------- | ------------------------------------- | ---------------------------------------------------------------- |
| What it does         | Changes the **same variable’s value** | Creates a **new variable with the same name**                    |
| Type change allowed? | ❌ No (must stay same type)            | ✅ Yes (can change type)                                          |
| Scope                | Same scope                            | New variable, same name — can also happen in a new inner scope   |
| Keyword needed       | `mut` only on first declaration       | Always use `let` again                                           |
| Purpose              | When you want to **update a value**   | When you want to **transform** or **redefine** a variable safely |
| Example use          | Counter, accumulator                  | Data transformation (e.g., trim → length)                        |

---

## 🧠 Think Like This

* **`mut` = “change this thing in place.”**
* **Shadowing = “redefine this name with a new meaning.”**

---

## 💻 Example 1 — Using `mut`

```rust
fn main() {
    let mut x = 5; // x = 5
    x = 6;          // ✅ changes same variable
    println!("x = {x}");
}
```

🧠 Same memory location, value changed.
Type cannot change.

---

## 💻 Example 2 — Using Shadowing

```rust
fn main() {
    let x = 5;
    let x = x + 1; // new variable, replaces old
    let x = x * 2; // another new variable
    println!("x = {x}"); // prints 12
}
```

🧠 Here, each `let` creates a **new variable** that hides (“shadows”) the old one.
Rust does not allow accidental mutation — you must *explicitly* say “new version”.

---

## 💻 Example 3 — Shadowing Changes Type (mut can’t)

```rust
fn main() {
    // Using shadowing ✅
    let spaces = "   ";
    let spaces = spaces.len(); // new var, different type (usize)
    println!("spaces = {spaces}");
}
```

```rust
fn main() {
    // Using mut ❌
    let mut spaces = "   ";
    spaces = spaces.len(); // error: mismatched types
}
```

🧠 `mut` can’t change type — because it’s the same variable.
Shadowing *creates a new one*, so type can differ.

---

## 🧾 When to Use Each

| Use Case                                                         | Recommended |
| ---------------------------------------------------------------- | ----------- |
| You want to **increment**, **accumulate**, or **change state**   | `mut`       |
| You want to **transform** a value safely (string → number, etc.) | Shadowing   |
| You want to **restrict mutation** but still refine meaning       | Shadowing   |
| You want to **change a variable in a loop or algorithm**         | `mut`       |

---

## 🔍 Real-world Analogy

* `mut` → Editing the same note repeatedly.
* Shadowing → Writing a new version of the note on a new page with same title.

You can’t accidentally mess with the old one because it’s replaced in a controlled way.


---

## 🧱 3️⃣ Constants in Rust

### 🧩 Definition

A **constant** is a *named value that never changes* — not at runtime, not anywhere.
It’s *immutable forever* (even stricter than `let` without `mut`).

---

### 🧠 Syntax

```rust
const MAX_POINTS: u32 = 100_000;
```

✅ Must always:

* Use `const` keyword
* Have an **explicit type** (`u32` here)
* Be assigned a **constant expression**, not a runtime value

---

### 💻 Example

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

fn main() {
    println!("There are {THREE_HOURS_IN_SECONDS} seconds in three hours!");
}
```

🧠 Here:

* `60 * 60 * 3` is a **compile-time** expression → allowed
* You **cannot** use something like:

  ```rust
  let x = 5;
  const VALUE: u32 = x * 2; // ❌ Error: x is runtime value
  ```

---

### ⚙️ Key Properties

| Property             | Meaning                                       |
| -------------------- | --------------------------------------------- |
| Always immutable     | Cannot use `mut` with `const`                 |
| Must have type       | Type must be declared (`u32`, `f64`, etc.)    |
| Compile-time known   | Value must be fully known before program runs |
| Global scope allowed | You can declare `const` outside `main()`      |
| Naming style         | All **UPPERCASE_WITH_UNDERSCORES**            |

---

### 🧾 Example — Global Constant

```rust
const SPEED_OF_LIGHT: f64 = 299_792_458.0; // meters per second

fn main() {
    println!("Speed of light = {SPEED_OF_LIGHT} m/s");
}
```

---

### 🔍 `let` vs `const` vs `mut`

| Keyword   | Mutable?              | Type Required? | Runtime or Compile-time | Can Shadow? | Typical Use                      |
| --------- | --------------------- | -------------- | ----------------------- | ----------- | -------------------------------- |
| `let`     | No                    | Optional       | Runtime                 | Yes         | Normal variable                  |
| `let mut` | Yes                   | Optional       | Runtime                 | No          | Counters, states                 |
| `const`   | No (always immutable) | **Required**   | **Compile-time only**   | No          | Fixed values (limits, constants) |

---

### ⚡ Example Comparison

```rust
fn main() {
    let mut score = 0;                 // ✅ runtime, mutable
    const MAX_SCORE: u32 = 100;        // ✅ compile-time, immutable

    score = 10;                        // ✅ works
    // MAX_SCORE = 200;                // ❌ cannot reassign constant

    println!("Score: {score}/{MAX_SCORE}");
}
```

---

### 💡 When to Use `const`

* Global settings (e.g., buffer sizes, time limits)
* Mathematical constants (`PI`, `SPEED_OF_LIGHT`)
* Any value known before runtime and used across files/modules

---

### 🏁 Summary

| Concept            | Keyword             | Can Change Value?   | Can Change Type? | Example                         |
| ------------------ | ------------------- | ------------------- | ---------------- | ------------------------------- |
| Immutable variable | `let`               | ❌                   | ❌                | `let x = 5;`                    |
| Mutable variable   | `let mut`           | ✅                   | ❌                | `let mut x = 5; x = 10;`        |
| Shadowed variable  | `let x = ...` again | ✅ (creates new var) | ✅                | `let x = "5"; let x = x.len();` |
| Constant           | `const`             | ❌ (compile-time)    | ❌                | `const PI: f64 = 3.14;`         |

