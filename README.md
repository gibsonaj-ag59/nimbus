# Vitruvius

## Overview

Vitruvius is a back end microprocess based architecture to support the ingest, cleaning, relating, storing and provision of data from multiple source devices collected by the Human Factors team.

## Prequisites

1. **Mac**

    1. Download and Install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).

        1. The [Docker Desktop Documentation](https://docs.docker.com/) is full of guides, manuals and references.
    
2. **Windows**

    1. Download and Install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).
        1. The [Docker Desktop Documentation](https://docs.docker.com/) is full of guides, manuals and references.

    2. Download and Install [The Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2)

        1. This [Microsoft Article](https://learn.microsoft.com/en-us/windows/wsl/about) has more information about WSL2 and what it does.

    3. Configure [Docker Desktop and WSL2](https://docs.docker.com/desktop/wsl/).

## Installation

Vitruvius is a cluster of Docker containers running in tandem. This splits the workload into multiple processes and allows a singular manager for all of those processes. To run a local **DEVELOPMENT** copy of Vitruvius. Clone this repository, ensure you have the prerequisites inplace, and use `docker compose up` in the [top folder](https://gitlab.stitches.mil/59-tes/vitruvius) of the repo.

### Components

---

The table belows shows nodes in the Vitruvius cluster.

| Name | Type | Enabled | Required | Function |
|-----------|--------------|-------|--------|----------------|
| vapi      | vtrvs_share  | True  | True   | Primary provider of data to the user |
| vmssql    | vtrvs_store  | False | False* | Microsoft SQL Server storage option |
| vredis    | vtrvs_store  | True  | True   | Provides a file store |
| vpostgres | vtrvs_store  | True  | True*  | PostgresSQL storage option |
| vconfig   | vtrvs_config | True  | True   | Configuration Management |
| vspydr    | vtrvs_model  | True  | True   | Spydr Data Management |

**Postgres is active by default. The system supports Microsoft SQL Server with some configuration changes. Having both storage systems active may cause unintended side affects.
 
## vapi

The v_api has a one endpoint style API. The endpoint is located at http://localhost:5554/api/v1/ and accepts a formatted query string as such: 

`<device>?<metric>-<comparison>=<criteria>`

> Only putting the device at the end of the URL:

http://localhost:5554/api/v1/spydr

will query everything for that device. Use with caution.

<details>
    <summary>Device Keywords</summary>
    <p>Must be one of the table names in <a href="https://gitlab.stitches.mil/59-tes/vitruvius/-/tree/main/models">the models</a> folder.</p>
</details>

<details>
    <summary>Metric Keywords</summary>
    <p>Must reference any column in the device's database table folder.</p>
</details>

<details>
    <summary>Comparison Operators</summary>
    <p>A list of Comparison Operators are in the table below</p>
    <table>
        <tr>
            <th>Operator</th>
            <th>Function</th>
        </tr>
        <tr>
            <td>eq</td>
            <td>equal to</td>
        </tr>
        <tr>
            <td>ne</td>
            <td>not equal to</td>
        </tr>
            <td>gt</td>
            <td>greater than</td>
        </tr>
        <tr>
            <td>ge</td>
            <td>greater than or equal to</td>
        </tr>
            <td>lt</td>
            <td>less than</td>
        </tr>
        <tr>
            <td>le</td>
            <td>less than or equal to</td>
        </tr>
    </table>
</details>

<details>
    <summary>Logical Operators</summary>
    <p>A list of Logical Operators are in the table below.</p>
    <table>
        <tr>
            <th>Operator</th>
            <th>Decoded</th>
            <th>Function</th>
        </tr>
        <tr>
            <td>&%2B&</td>
            <td>+</td>
            <td>AND</td>
        </tr>
        <tr>
            <td>&%7C&</td>
            <td>|</td>
            <td>OR</td>
        </tr>
    </table>
</details>

Requests can be made with multiple query statements by using Logical operators. To perform an OR operation seperate statements by `&%7C%&`. To perform an AND operation, seperate statements with `&%2B&`.

> Notice the `&` character preceeding and following each logical operator.

Example:

`http://localhost:5000/api/v1/spydr?l_pulserate-gt=90&%7C&r_pulserate-gt=90`

The above request will return any record from the Spydr node where the `l_pulserate` column, OR (`&%7C&`) `r_pulserate` column is greater than (`gt`) 90.

> Notice that Metric names use an underscore `_` for separation within itself and a dash `-` before the comparison operator.

## vspydr

The current configuration of the v_spydr data model has the following schema.

```json
"columns" : {
        "spydr_id": {
            "type": "Integer",
            "index": true
        },
        "datetime_utc": {
            "type": "DateTime"
        },
        "l_spo2" : {
            "type": "Integer"
        },
        "l_pulserate" : {
            "type": "Integer"
        },
        "l_status" : {
            "type": "Integer"
        },
        "l_pressure": {
            "type": "Integer"
        },
        "l_temperature": {
            "type": "Integer"
        },
        "l_accel_x": {
            "type": "Integer"
        },
        "l_accel_y": {
            "type": "Integer"
        },
        "l_accel_z": {
            "type": "Integer"
        },
        "l_gyro_x": {
            "type": "Integer"
        },
        "l_gyro_y": {
            "type": "Integer"
        },
        "l_gyro_z": {
            "type": "Integer"
        },
        "r_spo2" : {
            "type": "Integer"
        },
        "r_pulserate" : {
            "type": "Integer"
        },
        "r_status" : {
            "type": "Integer"
        },
        "r_pressure": {
            "type": "Integer"
        },
        "r_temperature": {
            "type": "Integer"
        },
        "r_accel_x": {
            "type": "Integer"
        },
        "r_accel_y": {
            "type": "Integer"
        },
        "r_accel_z": {
            "type": "Integer"
        },
        "r_gyro_x": {
            "type": "Integer"
        },
        "r_gyro_y": {
            "type": "Integer"
        },
        "r_gyro_z": {
            "type": "Integer"
        },
        "tvoc": {
            "type": "Integer"
        },
        "co2e_lowest": {
            "type": "Integer"
        },
        "co2e_highest": {
            "type": "Integer"
        },
        "resp_rate": {
            "type": "Integer"
        },
        "merged_spo2": {
            "type": "Integer"
        },
        "spo2_percent_difference":{ 
            "type": "Float"
        },
        "merged_pulserate": {
            "type": "Integer"
        },
        "pulserate_percent_difference": {
            "type": "Float"
        },
        "alarm":{
            "type": "Integer"
        },
        "tt":{ 
            "type": "Integer"
        },
        "elapsed_mission_time_mins": {
            "type": "Float"
        },
        "spo2_percent":{ 
            "type": "Integer"
        },
        "pulse_bpm":{   
            "type": "Integer"
        },
        "temp_f":{ 
            "type": "Integer"
        },
        "pressure_altitude_feet_msl":{ 
            "type": "Float"
        },
        "peak_acceleration_gs":{ 
            "type": "Float"
        },
        "hypox_alert":{ 
            "type": "Integer"
        },
        "baro_alert":{ 
            "type": "Integer"
        },
        "sortie_id":{ 
            "type": "Integer",
            "index": true
        }
    }
```