# Random Password Generator

**Decodelabs Project 3**

A tool that asks for a password length and generates a random, complex password from letters, numbers and (optionally) symbols. This repository contains two versions of the same idea:

- a **Python command-line program** (`password_generator.py`)
- a **web app** (`index.html`) that runs entirely in the browser

**Live demo:**   https://ridafatimazulfiqar.github.io/random-password-generator/

---

## Project goal

Write a tool that asks the user for a password length (e.g., 8 characters) and generates a random, complex password using letters and numbers.

**Key skills practised:** importing modules (`import random`) and string manipulation.

**Why it matters:** it shows how to use Python's built-in libraries to solve a real-world security problem.

---

## Features

| Feature | Python version | Web version |
|---|---|---|
| Choose password length | Typed input (minimum 4) | Slider (4 to 64) |
| Letters (A-Z, a-z) | Always included | Always included |
| Numbers (0-9) | Always included | Optional toggle |
| Symbols (`!@#$%` etc.) | Optional (y/n prompt) | Optional toggle |
| Guarantees one of each chosen type | Yes | Yes |
| Strength rating | Weak / Medium / Strong | Weak / Medium / Strong, with a bar and entropy in bits |
| Copy to clipboard | No | Yes |
| Input validation | Rejects non-numbers and lengths under 4 | Slider limits the range |

---

## Project structure

```
.
├── index.html             # Web version (HTML, CSS and JavaScript in one file)
├── password_generator.py  # Command-line version
└── README.md              # This documentation
```

---

## Getting started

### Python version

**Requirements:** Python 3.6 or newer. No extra packages are needed, because `random` and `string` are part of the standard library.

```bash
python password_generator.py
```

**Example session**

```
===================================
   RANDOM PASSWORD GENERATOR
===================================
Enter password length (e.g., 8): 12
Include symbols like @#$%? (y/n): y

Your generated password: k7#Qm2@xT9!b
Strength: Strong
```

### Web version

**Locally:** double-click `index.html` to open it in any modern browser. No server or build step is needed.

**On GitHub Pages:**

1. Push the files to a GitHub repository.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the `main` branch and the `/ (root)` folder, then click **Save**.
5. After a minute or two, the site is live at `https://<your-username>.github.io/<repository-name>/`.

---

## How it works

Both versions follow the same steps.

1. **Define the character sets.** Letters, digits and symbols are stored as strings.
2. **Guarantee variety.** One random character from each selected set is picked first, so the password can never be all letters.
3. **Fill the rest.** The remaining positions are filled with random characters from the combined pool.
4. **Shuffle.** The characters are shuffled so the guaranteed ones are not always at the start.
5. **Join.** The list of characters is joined into a single string.

### Python walkthrough

```python
import random
import string
```

The `random` module picks characters. The `string` module supplies ready-made character sets: `string.ascii_letters`, `string.digits` and `string.punctuation`.

| Function | Purpose |
|---|---|
| `generate_password(length, use_symbols)` | Builds the password using the five steps above. |
| `get_length()` | Keeps asking until the user enters a whole number of at least 4. |
| `main()` | Runs the program: prompts the user, generates the password and prints the strength rating. |

**String manipulation used:** `random.choice()` to pick characters, `random.shuffle()` to mix a list, and `"".join()` to turn a list of characters into a string.

**Strength rating (Python):**

| Condition | Rating |
|---|---|
| Length 12 or more and symbols included | Strong |
| Length 8 or more | Medium |
| Anything shorter | Weak |

### Web walkthrough

| Function | Purpose |
|---|---|
| `randInt(max)` | Returns an unbiased random integer using `crypto.getRandomValues`. |
| `pick(str)` | Picks one random character from a string. |
| `generate(length, useDigits, useSymbols)` | Builds the password and shuffles it with the Fisher-Yates algorithm. |
| `rate(length, poolSize)` | Estimates entropy and updates the strength bar. |
| `reveal(text)` | Plays a short scramble animation, skipped if the user prefers reduced motion. |
| `copy()` | Copies the password to the clipboard, with a fallback for older browsers. |

**Strength rating (web):** it is based on entropy, calculated as `length × log2(pool size)`.

| Entropy | Rating |
|---|---|
| Under 50 bits | Weak |
| 50 to 79 bits | Medium |
| 80 bits or more | Strong |

---

## Security notes

- **The Python version uses `random`**, which is fine for learning but is not designed for security. For real-world passwords, replace it with the `secrets` module (`secrets.choice()` instead of `random.choice()`). It draws from the operating system's secure random source.
- **The web version already uses `crypto.getRandomValues`**, a cryptographically secure source, and avoids modulo bias.
- **Nothing is sent anywhere.** The web app makes no network requests for passwords, and nothing is stored.
- **Use a password manager** to store generated passwords.

---

## Browser support

Works in current versions of Chrome, Edge, Firefox and Safari. Copy-to-clipboard needs HTTPS or `localhost` for the modern API and falls back to an older method otherwise. The page follows the system light or dark theme.

---

## Possible improvements

- Switch the Python version to the `secrets` module.
- Add an option to exclude look-alike characters such as `O`, `0`, `l` and `1`.
- Generate several passwords at once.
- Add a passphrase mode made of random words.
- Add unit tests that check length, character types and variety.

---

## Author

Created as part of the **Decodelabs** internship, Project 3.
