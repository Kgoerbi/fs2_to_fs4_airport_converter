-------------------- UNDER CONSTRUCTION --------------------


# Object

IPACS now offers the **[Aerofly FS Flight Simulator](https://www.aerofly.com)** in version **FS 4**.

For the previous version **FS 2** there are more than 3,500 airports in over 180 countries in the **[FSCloudport](https://www.fscloudport.com)**. When downloading an airport, a folder with its [ICAO code](https://en.wikipedia.org/wiki/ICAO_airport_code) is created and the airport-specific files are stored in this folder. The most important data are in the two text files ICAO.TOC and ICAO.TSC.

Compared to FS 2, the aerodromes in **FS 4** function in a simpler structure with considerably less data. Among other things, the data of the two text files are now combined in a text file ICAO.TAP, which can be edited with a text editor and/or imported into the AirportCreationTool (ACT) and/or converted with the [airport TAP converter (see this article in the Aerofly Forum)](https://www.aerofly.com/community/forum/index.php?thread/19827-aerofly-fs-airport-creation-tool-early-alpha-version-work-in-progress/&postID=123276#post123276) and used in FS 4.

**The software "fs2_to_fs4_airport_converter" generates the ICAO.TAP file for FS 4 from the previous ICAO.TOC and ICAO.TSC files for FS 2 and transfers all data.**


# Data

These data are inserted into the TAP file

* from the TSC file:
  * from General: `icao`, `iata`, `name`, `name_short`, `country`, `elevation`, `model_center`.
  * from Tower: `tower_position`, `tower_height`, `tower_view_height`.
  * from Runway: `threshold`, `identifier`, `appltsys`, `reil`, `papi`, `widht` 
  * from Parking: `position`, `direction`, `name`
  * from Helipad: `position`, `direction`, `radius`, `name`

* from the TOC file:
  * from xref: `name`, `position`, `direction` (this converts FS 2`orientation` to FS 4-`direction`)

* added as default values:
  * for Tower: `tower_heading [0]`
  * for Runway: `extension [0]`, `direction []`, `elevation] []`, `approach [false]`, `takeoff [false]`, `marking_piano [false]`, `marking_touchdown [false]`, `marking_threshold [false]`, `marking_aimingpoint [false]`, `marking_nonumbers [true]`, `marking_skidmark [false]`, `material [asphalt_runway__typestd]`, `brightness [0. 5]`, `marking_centreline [true]`, `marking_sidelines [false]`
  * for Parking: `radius [40]`, `type [parked_jet]`.
  * for Boundaries: `points [(lon+0.04 lat+0.02) (lon+0.04 lat-0.02) (lon-0.04 lat-0.02) (lon-0.04 lat+0.02) (lon+0.04 lat+0.02)]`


# Installation / Deinstallation

## Installation

UNDER CONSTRUCTION

## Deinstallation

UNDER CONSTRUCTION


# Funktion

UNDER CONSTRUCTION


# Anwendung

UNDER CONSTRUCTION
