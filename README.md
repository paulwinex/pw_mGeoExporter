# mGeo Exporter v1.2
##### (Recreated repository)

New repository with new version.

### Whats new in v1.2?

- Support Maya 2017 and PySide 2 (not stable)
- Export Alembic Point Cache + HDA to read this cache
- New convenient table for create custom export attributes
- Now you can save options presets to file and quick load back to export set
- Frame padding for cache
- Compress geo and bgeo to new SC archive (Houdini14)

Full feature list you can found in manuals

### install
1. Copy folder pw_mGeoExporter to the PYTHONPATH folder
2. In ScriptEditor execute code:
```python
import pw_mGeoExporter
pw_mGeoExporter.show()
```