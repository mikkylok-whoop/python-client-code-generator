#!/bin/bash
set -e

# Package settings
PACKAGE_NAME="data_sci_mdas"
VERSION="0.0.4"

# Configuration
WORKSPACE_DIR="$HOME/whoop_projects/test-python-client-generator"
INPUT_SPEC="$WORKSPACE_DIR/data-sci-mdas_openapi.json"
OUTPUT_DIR="$WORKSPACE_DIR/generator"
TEMPLATE_DIR="$WORKSPACE_DIR/custom_templates"
PACKAGE_OUTPUT_DIR="$HOME/PycharmProjects/test_python_client_code_gen"

echo "Generating client version $VERSION..."

echo "Step 1: Generating client..."
openapi-generator generate \
  -g python-pydantic-v1 \
  -i "$INPUT_SPEC" \
  -o "$OUTPUT_DIR" \
  -t "$TEMPLATE_DIR" \
  --additional-properties=packageName="$PACKAGE_NAME",packageVersion="$VERSION"

echo "Step 2: Keeping only necessary files..."
# Create a temporary directory to save essential files
mkdir -p "$WORKSPACE_DIR/temp_save"

# Save only what we need
cp -r "$OUTPUT_DIR/$PACKAGE_NAME/api" "$WORKSPACE_DIR/temp_save/"
cp -r "$OUTPUT_DIR/$PACKAGE_NAME/models" "$WORKSPACE_DIR/temp_save/"
#cp "$OUTPUT_DIR/$PACKAGE_NAME/__init__.py" "$WORKSPACE_DIR/temp_save/"
cp "$OUTPUT_DIR/pyproject.toml" "$WORKSPACE_DIR/temp_save/"

# Remove everything from the output directory, including hidden files
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Recreate the package directory
mkdir -p "$OUTPUT_DIR/$PACKAGE_NAME"

# Move saved files back
cp -r "$WORKSPACE_DIR/temp_save/api" "$OUTPUT_DIR/$PACKAGE_NAME/"
cp -r "$WORKSPACE_DIR/temp_save/models" "$OUTPUT_DIR/$PACKAGE_NAME/"
touch "$OUTPUT_DIR/$PACKAGE_NAME/__init__.py"
cp "$WORKSPACE_DIR/temp_save/pyproject.toml" "$OUTPUT_DIR/"

# Clean up temp directory
rm -rf "$WORKSPACE_DIR/temp_save"

echo "Step 3: Setting up Poetry environment..."
cd "$OUTPUT_DIR"
# Ensure Poetry uses the correct Python version
if command -v pyenv &> /dev/null; then
poetry env use $(pyenv which python)
else
  poetry env use python3
fi

echo "Step 4: Installing dependencies..."
poetry install

echo "Step 4.5: Running linters and type checkers..."

echo "Running isort..."
poetry run isort "$PACKAGE_NAME"

echo "Running black..."
poetry run black "$PACKAGE_NAME"

#echo "Running mypy..."
#poetry run mypy "$PACKAGE_NAME"

echo "Step 5: Building the package..."
poetry build

echo "Step 6: Moving package to output directory..."
mkdir -p "$PACKAGE_OUTPUT_DIR"
# Move the entire dist folder instead of just its contents
mv "$OUTPUT_DIR/dist" "$PACKAGE_OUTPUT_DIR/"

echo "Done! Package built successfully with version $VERSION."
echo "Package artifacts are in: $PACKAGE_OUTPUT_DIR/dist"