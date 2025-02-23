## Purpose of the Script

This script generates an interactive rotating globe, allowing users to explore country geometries 
using `geopandas` and visualize the data with `plotly`. It provides a simple way to visualize geospatial data interactively 
and can be extended for other visualizations involving geographic datasets.

## Steps Followed

1. Created a new directory for the project inside the Git repository.
2. Set up a Python virtual environment using `python -m venv venv`.
3. Activated the virtual environment and installed required dependencies (`geopandas`, `pandas`, `plotly`, `requests`).
4. Generated a full requirements file (`all_requirements.txt`) using `pip freeze`.
5. Cleaned the `requirements.txt` file using `pipdeptree` and `pipreqs` to include only the necessary dependencies.
6. Removed all installed packages to simulate a clean environment.
7. Reinstalled the required dependencies from `requirements.txt`.
8. Verified that the script works as expected by running the interactive globe.
9. Analyzed the project’s dependencies using `pipdeptree`.
10. Created and documented the process in this `README.md` file.


## Output of pipdeptree

geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
pipreqs==0.4.13
  - docopt [required: Any, installed: 0.6.2]
  - yarg [required: Any, installed: 0.1.10]
    - requests [required: Any, installed: 2.32.3]
      - certifi [required: >=2017.4.17, installed: 2025.1.31]
      - charset-normalizer [required: >=2,<4, installed: 3.4.1]
      - idna [required: >=2.5,<4, installed: 3.10]
      - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]

## Observations or Issues

- During the installation of dependencies, I encountered an issue where some dependencies had conflicting versions. This was resolved by ensuring that all packages were compatible with each other using `pipdeptree`.
- The interactive globe works as expected and it runs very smooth.
- Using `pipreqs` was useful in reducing unnecessary packages in the `requirements.txt` file.
