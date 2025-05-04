# Changelog

## Fix unsupported glob pattern in pyproject.toml exclude list

- The exclude pattern "**/@test" in the `[tool.hatch.build]` section of `pyproject.toml` caused an "Unsupported glob expression" error when using the uv_build backend.
- Updated the pattern to the more specific `"src/**/@test/**"` to avoid the error and correctly exclude the in-package `@test` directories.
- This change ensures compatibility with the uv_build backend's glob pattern parser while maintaining the intended exclusion of test directories.
