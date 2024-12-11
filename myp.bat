@echo off
c:
SET OSGEO4W_ROOT=C:\OSGeo4W
SET QGISNAME=qgis
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

@echo on
call "%OSGEO4W_ROOT%\apps\Python312\Scripts\pyrcc5" -o resources.py resources.qrc

pause