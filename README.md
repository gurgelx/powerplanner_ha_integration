# PowerPlanner for Home Assistant

This [Home Assistant](https://www.home-assistant.io/) integration allows you to use your PowerPlanner plans on Home Assistant as sensors

## Installation

**Method 1.** [HACS](https://hacs.xyz/) custom repo:

> HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: `gurgelx/powerplanner_ha_integration`, Category: Integration > Add > wait > PowerPlanner > Install

**Method 2.** Manually copy `powerplanner` folder under `custom_components` from [latest release](https://github.com/gurgelx/powerplanner_ha_integration) to `/config/custom_components` folder.

## Configuration

**Add integration**:
1. Get the API key from your account on [PowerPlanner](https://www.powerplanner.se/)
> Login > Click on your name > Click API > Copy the API key
2. Add the integration
> Configuration > Integrations > Add Integration > **PowerPlanner**

> Paste the key in the prompt for `API KEY`

If the integration is not in the list, you need to clear the browser cache.

## Usage
The integration will automatically sync with powerplanner.se within an interval.

If you don't want to wait for your changes to show up you can use the sync button:
> Settings > Device & Services > 1 Device on the PowerPlanner card > Sync PowerPlanner

Your sensors will show up on the powerplanner device and can be used as any binary_sensor.
