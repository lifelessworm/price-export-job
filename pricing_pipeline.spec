# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pricing_pipeline.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['getpass'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    # NOTE: kept as 'mestre' intentionally so the built executable's filename
    # (dist/mestre.exe) doesn't change. If a Windows Task Scheduler job or
    # .bat file elsewhere points at mestre.exe, changing this name would
    # silently break that job. Rename here (and update the scheduled task)
    # if/when you're ready to retire the old executable name.
    name='mestre',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
