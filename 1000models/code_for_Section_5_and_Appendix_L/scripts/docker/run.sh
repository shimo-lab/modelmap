#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Run the model_map container with volume mounts using absolute host paths.
#   • The current directory is mounted to /workspace inside the container.
#   • The ../data directory (relative to this script) is mounted to /data.
#   • Works on macOS (Darwin) and GNU/Linux.
# -----------------------------------------------------------------------------
set -euo pipefail  # Exit on error, unset vars are errors, pipelines propagate errors.

# -------------------------------------------------
# Helper: abspath <relative_path>
#   Returns an absolute, canonical path or exits with an error if the required
#   utilities are not available on the host OS.
# -------------------------------------------------
abspath () {
  local target="$1"

  case "$(uname -s)" in
    Darwin*)  # macOS
      if command -v greadlink >/dev/null 2>&1; then
        greadlink -f "$target"           # Preferred (brew install coreutils)
      elif command -v realpath >/dev/null 2>&1; then
        realpath "$target"               # Fallback if realpath exists
      else
        echo "Error: install coreutils (greadlink) or realpath on macOS." >&2
        exit 1
      fi
      ;;
    *)        # GNU/Linux, WSL, *BSD, etc.
      if command -v readlink >/dev/null 2>&1; then
        readlink -f "$target"            # Requires GNU readlink with -f
      else
        echo "Error: readlink -f is required on this platform." >&2
        exit 1
      fi
      ;;
  esac
}

# -------------------------------------------------
# Resolve host paths
# -------------------------------------------------
HOST_WORKSPACE=$(pwd)             # Absolute path of the current directory
HOST_DATA=$(abspath ../data)      # Absolute path of ../data

# Optional: echo paths for debugging
# echo "HOST_WORKSPACE=${HOST_WORKSPACE}"
# echo "HOST_DATA=${HOST_DATA}"

# -------------------------------------------------
# Launch Docker container
# -------------------------------------------------
docker run --rm -it --name model_map \
  -u "$(id -u):$(id -g)" \
  -v "${HOST_WORKSPACE}:/workspace" \
  -v "${HOST_DATA}:/data" \
  "${USER}/model_map" bash
