# Buienradar plugin

De buienradar plugin is gemaakt om de buienradar data (die openlijk beschikbaar is op buienradar) geografisch weer te kunnen geven. Hierbij worden de symbolen van de buienradar gebruikt om het geheel te visualiseren.

De enige vereiste is QGIS zelf.

De plugin is te installeren via QGIS.

Hieronder is een afbeelding te zien van de simpele interface. Je kunt een achtergrond kiezen en wanneer je daarna op de OK knop drukt wordt alle data ingeladen in je hoofdscherm.

![Hoofdscherm](readme_afbeeldingen/hoofdscherm.PNG)

## Lokaal testen tijdens ontwikkelen

De plugin heeft geen buildstap nodig: code wordt rechtstreeks door QGIS geladen. Om wijzigingen in deze repo direct te zien in QGIS, maak je een *directory junction* aan vanuit de pluginmap van je QGIS-profiel naar deze repo. Een junction vereist geen administratorrechten op Windows.

```powershell
New-Item -ItemType Junction `
  -Path "$env:APPDATA\QGIS\QGIS4\profiles\default\python\plugins\buienradar_plugin" `
  -Target "<pad naar deze repo>"
```

Vink daarna in QGIS de plugin aan via **Plugins > Manage and Install Plugins > Installed**.

Installeer ook de core-plugin **Plugin Reloader** (via Manage and Install Plugins). Na een codewijziging klik je simpelweg op het Plugin Reloader-icoon om de Buienradar plugin opnieuw te laden, zonder QGIS te herstarten.

## Releasen naar de QGIS plugin repository

1. **Versie bumpen.** Verhoog `version=` in [metadata.txt](metadata.txt) en voeg een regel toe aan de `changelog=`.
2. **Zip bouwen.** De zip moet een map `buienradar_plugin/` als root hebben met alleen de uit te leveren bestanden (geen `test/`, `Makefile`, `.git`, ...):
   - Aanrader: `pip install pb_tool` en dan `pb_tool zip` (gebruikt de bestandenlijst uit [pb_tool.cfg](pb_tool.cfg)).
3. **Uploaden**: inloggen op plugins.qgis.org met het account dat eigenaar is van de plugin, naar de plugin-pagina, nieuwe versie uploaden.
4. **Controleren.** Na upload valideert de repository het pakket en publiceert de nieuwe versie.

## Contact

Contributor: Peter Schols

Voor meer informatie kunt u mailen naar: jeroenvanderzwam@hotmail.com
