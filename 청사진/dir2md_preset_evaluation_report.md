# dir2md Preset Evaluation Report

## 1. Introduction

This report provides a detailed analysis and evaluation of the three core presets available in the `dir2md` tool: `iceberg`, `pro`, and `raw`. The evaluation is based on a direct analysis of the tool's source code (`core.py`) to explain the precise behavior of each preset.

---

## 2. Preset Analysis

### 🧊 `iceberg`

This is the **smart, adaptive preset designed for AI and LLMs**. Its primary goal is to generate the most useful, context-aware summary of a project that fits within a typical LLM's context window.

*   **Philosophy:** Show the "tip of the iceberg." Prioritize the most important information and intelligently reduce verbosity based on project size.
*   **Key Settings Applied:**
    *   `respect_gitignore`: `True` (Ignores files listed in `.gitignore`).
    *   `dedup_bits`: `16` (Enables deduplication to remove similar/duplicate files).
    *   `emit_manifest`: `True` (Creates a `manifest.json` file with metadata about the output).
    *   `only_ext`: Defaults to a list of common source code extensions (e.g., `.py`, `.js`, `.md`).
    *   **`llm_mode` (Automatic):** This is the core feature. The preset automatically selects the content mode based on the total size of the project:
        *   **Small Projects (<200KB):** `inline` mode (includes full file content).
        *   **Medium Projects (200KB - 5MB):** `summary` mode (includes an AI-generated summary of each file).
        *   **Large Projects (>5MB):** `ref` mode (includes only file paths and metadata, no content).
*   **Evaluation:**
    *   **Best For:** AI analysis, providing project context to an LLM, and automated documentation.
    *   **Conclusion:** This is the most advanced and recommended preset for any AI-driven task.

### 💼 `pro`

This is the **manual or "professional" preset**. It acts as a blank slate, applying no automatic configurations. It is designed for power users who want to fine-tune the output using the tool's many command-line arguments.

*   **Philosophy:** The user is the "pro" and has full control.
*   **Key Settings Applied:**
    *   None. The preset simply allows the tool's default settings or the user's explicitly provided flags to take effect.
*   **Evaluation:**
    *   **Best For:** Users who want to experiment with different configurations or have a very specific output requirement.
    *   **Conclusion:** Use this preset when you want to build your own configuration from the ground up by providing arguments like `--llm-mode`, `--budget-tokens`, `--only-ext`, etc.

### 📜 `raw`

This is the **unfiltered, "dump everything" preset**. Its goal is to create the most complete and literal representation of the directory, with minimal processing.

*   **Philosophy:** What you see is what you get. Every file and all of its content.
*   **Key Settings Applied:**
    *   `llm_mode`: `inline` (Always attempts to include the full content of every file).
    *   `dedup_bits`: `0` (Disables deduplication).
    *   `only_ext`: `None` (Includes all files, regardless of extension).
    *   `emit_manifest`: `False` (Does not create a manifest file).
*   **Evaluation:**
    *   **Best For:** Creating a complete, local archive of a project in a single text file.
    *   **Conclusion:** While comprehensive, the output can be excessively large and difficult for either a human or an AI to parse, especially for large projects.

---

## 3. Comparison Summary

| Feature                  | 🧊 `iceberg`                  | 💼 `pro`         | 📜 `raw`            |
| :----------------------- | :---------------------------- | :--------------- | :------------------ |
| **Primary Use Case**     | **AI Analysis**               | **Manual Control** | **Archiving**       |
| **LLM Mode**             | Auto (inline/summary/ref)     | User-defined     | Always `inline`     |
| **Deduplication**        | Enabled                       | User-defined     | Disabled            |
| **Respects `.gitignore`**| Yes                           | User-defined     | No (by default)     |
| **File Types**           | Common code files (default)   | User-defined     | All files           |
| **Manifest File**        | Yes                           | User-defined     | No                  |

---

## 4. Final Recommendation

*   **For AI Interaction & Analysis:** Always use **`iceberg`**. It provides the best balance of detail and brevity, tailored for LLM consumption.
*   **For Full Control:** Use **`pro`** when you need to customize the output beyond what `iceberg` offers.
*   **For Archiving:** Use **`raw`** only when you need a complete, unfiltered text backup of a directory.
