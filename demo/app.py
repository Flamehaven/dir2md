import gradio as gr
import git
import tempfile
import shutil
from pathlib import Path
import os

# dir2md will be imported from the source code uploaded to the Space.
from dir2md.core import generate_markdown_report, Config

def process_github_repo(repo_url: str, preset: str):
    """
    Clones a GitHub repository and generates a dir2md blueprint.
    """
    temp_dir_path = None
    try:
        # 1. Create a temporary directory
        temp_dir_path = tempfile.mkdtemp()
        temp_dir = Path(temp_dir_path)

        # 2. Clone the Git repository
        gr.Info(f"Cloning repository: {repo_url}...")
        git.Repo.clone_from(repo_url, temp_dir)
        gr.Info("Repository cloned. Generating blueprint...")

        # 3. Create a dir2md Config object
        # The output path is temporary as we return the content as a string.
        output_path = temp_dir / "blueprint.md"

        cfg = Config(
            root=temp_dir,
            output=output_path,
            preset=preset,
            # Default values
            include_globs=[],
            exclude_globs=[],
            omit_globs=[],
            respect_gitignore=True,
            follow_symlinks=False,
            max_bytes=None,
            max_lines=None,
            include_contents=True,
            llm_mode="ref",
            budget_tokens=8000,
            max_file_tokens=2000,
            dedup_bits=16,
            sample_head=120,
            sample_tail=40,
            strip_comments=False,
            emit_manifest=False, # No manifest file needed for the demo
            explain_capsule=False,
            no_timestamp=True,
            masking_mode="basic"
        )

        # 4. Call the blueprint generation function
        md_output = generate_markdown_report(cfg)
        gr.Info("Blueprint generated successfully!")

        return md_output

    except Exception as e:
        # Clean up the temp directory on error
        if temp_dir_path and os.path.exists(temp_dir_path):
            shutil.rmtree(temp_dir_path)
        return f"An error occurred: {e}"
    finally:
        # 5. Delete the temporary directory
        if temp_dir_path and os.path.exists(temp_dir_path):
            shutil.rmtree(temp_dir_path)

# 6. Define the Gradio interface
demo = gr.Interface(
    fn=process_github_repo,
    inputs=[
        gr.Textbox(label="GitHub Repository URL", placeholder="https://github.com/Flamehaven/dir2md"),
        gr.Radio(choices=["iceberg", "raw", "pro"], value="iceberg", label="Select Preset")
    ],
    outputs=gr.Textbox(label="Markdown Blueprint", lines=30, show_copy_button=True),
    title="dir2md: AI-Ready Repository Blueprint Generator",
    description="Enter the URL of a public GitHub repository to convert its structure and content into an LLM-friendly Markdown blueprint.",
    allow_flagging="never",
    examples=[["https://github.com/psf/requests", "iceberg"], ["https://github.com/gradio-app/gradio", "raw"]]
)

demo.launch()