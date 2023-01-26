import kaggle

kaggle datasets list -s 'world by population 2022'

kaggle datasets download -d "anandhuh/countries-in-the-world-by-population-2022"

mv /workspaces/bts_jewel/"countries-in-the-world-by-population-2022.zip" /workspaces/bts_jewel/downloads/

unzip /workspaces/bts_jewel/downloads/"countries-in-the-world-by-population-2022.zip" -d data/