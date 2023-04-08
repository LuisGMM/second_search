# Delta docs example

## 📄 Building documentation

In order to build documentation it is required to fork or download this repository to your local machine, see previous sections. Once this task is done, follow these steps:

0. Climb to delta_docs_example parent directory `cd ../`, and then run:

    ```bash
    pip install --editable delta_docs_example/[docs]
    ```

1. Move to `docs/` directory by running:

    ```bash
    cd delta_docs_example/docs/
    ```

2. The docs are built with `Sphinx`, which allows multiple output formats. Make sure a `Makefile` file exists within `docs/` directory. Check for available output options by running:

    ```bash
    make help
    ```

3. Once you select your desired output (in this case HTML) execute it:

    ```bash
    make html
    ```

4. For PDFs, a simple PDF reader would work. Open the generated HTML files with a browser:

    ```bash
    firefox build/html/index.html
    ```

5. To convert interactive examples into plain Python scripts, run:

    ```bash
    make examples
    ```

    This Makefile rule calls `jupytext` to convert the Markdown notebooks into Python scripts.

6. Alternatively to all previous workflow, you can also run:

   ```bash
   make docs && firefox/docs/build/html/index.html
   ```

   within delta_docs_example's project folder. This command will build and open the rendered documentation in the browser.
