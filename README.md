# Lizenz

This work is licensed under **Creative Commons Attribution-NonCommercial 4.0 International License** ([short description](https://creativecommons.org/licenses/by-nc/4.0/deed.en) / [copy of this license](https://creativecommons.org/licenses/by-nc/4.0/legalcode)).


# Object

IPACS offers the **[Aerofly FS Flight Simulator](https://www.aerofly.com)** in version **FS 4**.

For the previous version **FS 2** there are more than 3,500 aerodromes in over 180 countries in the **[FSCloudport](https://www.fscloudport.com)**. When downloading an aerodrome, a folder with its [ICAO code](https://en.wikipedia.org/wiki/ICAO_airport_code) is created and the aerodrome-specific files are stored in this folder. The most important data are in the two text files ICAO.TOC and ICAO.TSC.[^1]

Compared to FS 2, the aerodromes in **FS 4** function in a simpler structure with considerably less data. Among other things, the data of the two text files are now combined in one text file ICAO.TAP, which can be edited with a text editor and/or imported into the [Airport Creation Tool (currently in alpha testing)](https://tap-user.aerofly.com) and/or converted with the [airport TAP converter (see this article in the Aerofly Forum)](https://www.aerofly.com/community/forum/index.php?thread/19827-aerofly-fs-airport-creation-tool-early-alpha-version-work-in-progress/&postID=123276#post123276) and used in FS 4.

**The software "fs2_to_fs4_airport_converter" generates the ICAO.TAP file for FS 4 from the previous ICAO.TOC and ICAO.TSC files for FS 2 and transfers all data.**

The software has been tested with **MacOS** and **WindowsOS**.

[^1]: The letters "ICAO" in file and directory names act as placeholders for the ICAO codes of airports (e.g. EGLL for London Heathrow Airport) or comparable codes for smaller airfields (e.g. GB0001 for RAF Barford St .John).


# Data

These data[^2] are inserted into the TAP file:

* from the TSC file:
  * from General: `icao`, `iata`, `name`, `name_short`, `country`, `elevation`, `model_center`
  * from Tower-View: `tower_position`, `tower_height`, `tower_view_height`
  * from Runway: `threshold`, `identifier`, `appltsys`, `reil`, `papi`, `widht` 
  * from Parking: `position`, `direction`, `name`
  * from Helipad: `position`, `direction`, `radius`, `name`

* from the TOC file:
  * from xref: `name` (changed from uppercase to lowercase), `position`, `direction` (converted from FS 2-orientation to FS 4-`direction`)

* added as default values:
  * for Tower-View: `tower_heading [0]`
  * for Runway: `extension [0]`, `direction []`, `elevation] []`, `approach [false]`, `takeoff [false]`, `marking_piano [false]`, `marking_touchdown [false]`, `marking_threshold [false]`, `marking_aimingpoint [false]`, `marking_nonumbers [true]`, `marking_skidmark [false]`, `material [asphalt_runway__typestd]`, `brightness [0.5]`, `marking_centreline [true]`, `marking_sidelines [false]`
  * for Parking: `radius [40]`, `type [parked_jet]`
  * for Boundaries: `points [(lon+0.04 lat+0.02) (lon+0.04 lat-0.02) (lon-0.04 lat-0.02) (lon-0.04 lat+0.02) (lon+0.04 lat+0.02)]`

[^2]: The terms are the names in FS 4.

# Installation / Deinstallation

## Installation

When downloading, the folder "fs2_to_fs4_airport_converter-main" with the subfolder "fs2_to_fs4_airport_converter" is automatically created.

* move the subfolder "fs2_to_fs4_airport_converter" to a location accessible from the TERMINAL

## Deinstallation

* delete the folder "fs2_to_fs4_airport_converter"


# Use

## 1. Download

* load the desired FS 2 aerodromes from [FSCloudPort](https://www.fscloudport.com) into the directory "..path../**fs2_to_fs4_airport_converter/input/..**"

==> The downloaded ICAO.ZIP files can then be found here as "..path../fs2_to_fs4_airport_converter/**input/ICAO.ZIP**".

## 2. Unzip

* unzip the ICAO.ZIP files

==> Unzipping creates for each ICAO.ZIP its own folder "..path../fs2_to_fs4_airport_converter/**input/ICAO/..**" and saves the associated files in these, of which only the two files **ICAO.TOC** and **ICAO.TSC** are necessary.

* delete the ICAO.ZIP files

## 3. Convert

* open TERMINAL
* switch to the program folder with `cd ..path../fs2_to_fs4_airport_converter/python_scripts`
* start the program with `python3 main.py`

==> The program creates for each aerodrome one FS 4 file ICAO.TAP from the two FS 2 files ICAO.TOC and ICAO.TSC and saves this under "..path../fs2_to_fs4_airport_converter/**output/ICAO.TAP**".

This process may take a few seconds:
- If the program has run through without errors, the cursor will then appear in the TERMINAL at the input point as before the program started.
- If there are errors, the ICAO codes of the affected aerodromes are listed in the TERMINAL. **The only known errors** so far are letters in the `name` and `name_short` fields that do not correspond to the ASCII code. These letters must then be replaced by ASCII-compliant characters.


# Applications after converting

The TAP files can now be used.

## 1. Convert and Import in FS 4

With [airport TAP converter (see this article in the Aerofly Forum)](https://www.aerofly.com/community/forum/index.php?thread/19827-aerofly-fs-airport-creation-tool-early-alpha-version-work-in-progress/&postID=123276#post123276) the TAP files are converted for direct use in FS 4. An "icao" folder with the four files "icao.tmb", "icao.toc", "icao.tsc" and "icao.wad" is created for each aerodrome and placed in the user folder (e.g. on Mac: "/Users/[loginname]/Library/Application Support/Aerofly FS 4/**scenery/airports/ICAO/..**"; e.g. on Windows: "C:/Users/username/Documents/Aerofly FS 4/**scenery/airports/ICAO/..**").

These aerodromes in FS 4 are at the same level as FS 2 and lack the FS 4 features:
* Towers (xref, not tower_view) face east (`direction [90]`).
* Runways have a standard design (see "Data" above).
* Parking positions have a standard design (see "Data" above).
* Imported buildings may overlap with existing automatic buildings.

## 2. Editing with a text editor

The TAP files have content similar to that described in the [AEROFLY FS WIKI for FS 2](https://www.aerofly.com/dokuwiki/doku.php/start) in the "Developer / Scenery Development" section.

After editing with a text editor, the TAP files can then be used in FS 4 as described under "1. Convert and Import in FS 4".

## 3. Import in Airport Creation Tool

The TAP files can be integrated directly into the [Airport Creation Tool (currently in alpha testing)](https://tap-user.aerofly.com) and further edited there.

An **error** occurs during import if the TAP file contains an xref element that is not present in the Airport Creation Tool - then the displayed xref element in the TAP file must be deleted (!).
