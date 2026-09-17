## Transportation Network Analysis with Graph Theory 🚚
*Use the graph theory to optimise the road transportation network of a retail company*

<p align="center">
  <a href="https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://cdn-images-1.medium.com/max/800/1*J0KtD5r1x0JUTt_YeI2QRA.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

### Objective
Build graphical representations of a road transportation network to support network optimisation studies.

### Introduction
For a retailer, road transportation between the distribution centre and stores accounts for a significant share of logistics costs. 
Companies often conduct route-planning optimisation studies to reduce these costs and improve network efficiency.

It requires **collaboration** between continuous improvement engineers and the transportation teams that manage operations daily.

### 📘 Your complete guide for Supply Chain Analytics
60+ case studies with source code, dummy data and mathematical concepts here 👉 [Analytics Cheat Sheet](https://abstracted-hydrant-a3d.notion.site/Supply-Chain-Analytics-Cheat-Sheet-d449e3d53cfc45978aa889d3ef40f559?pvs=4)

### Article
In this [Article](https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/), we will use Graph Theory to design visual representations of a transportation network to support this collaboration and facilitate solution design.

### Youtube Video
Click on the image below to access a full tutorial video to understand the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=lhDBTlsGDVc"><img src="https://i.ytimg.com/vi/lhDBTlsGDVc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFTyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBW3XmI1zkXElOVtqEQFBBJV-ctrw" alt="Explainer Video Link"></a>
</div>

### Scenario
As a **continuous improvement engineer** of a retail company, you are in charge of reengineering warehousing and transportation operations. In your scope, you have a major distribution centre located in Shanghai (China) that delivers **54 hypermarkets**.
<p align="center">
  <a href="https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://cdn-images-1.medium.com/max/800/1*RIXTE99d2grMCtvy5g_0EQ.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

#### Objective
Your objective is to reduce the total cost of transportation.

#### Insights: Cost per Ton
The objective is to design  a new transportation plan to increase the average truck size by delivering more stores per route.
<p align="center">
  <a href="https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://cdn-images-1.medium.com/max/800/1*UCtbo4w43ZghEHtXtTuVuQ.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>
                                                                                               
#### Solution: Graph Theory
A graph is a structure that consists of nodes (vertices) and edges, where each edge connects two nodes.
<p align="center">
  <a href="https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://cdn-images-1.medium.com/max/800/1*YqUdhRzq9vHfuslfKFInCA.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

#### Further Analysis
With these graphs, you can challenge the current routing and discuss optimisation levers with the transportation teams.
<p align="center">
  <a href="https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://cdn-images-1.medium.com/max/800/1*vrsJmzuXzrFMy_qA4FuvVg.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>
                                                                                               

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Network Graph.ipynb` - Jupyter notebook with step-by-step analysis
- `network_graph.py` - Standalone Python script
- `data/` - Folder containing input data (store province.xlsx, delivery records.xlsx)

### Getting Started
```bash
pip install -r requirements.txt
python network_graph.py
```

### Dependencies
- numpy
- pandas
- matplotlib
- networkx
- openpyxl

## Go further

- **The full write-up, with the reasoning behind the code:** [Transportation Network Analysis with Graph Theory](https://www.samirsaci.com/transportation-network-analysis-with-graph-theory/?utm_source=github&utm_medium=readme&utm_campaign=graph-theory)
- **The video:** [Transportation Network Analysis with Graph Theory](https://youtu.be/lhDBTlsGDVc)
- **Test what you learned:** the [Supply Science App](https://supply-science.com/?utm_source=github&utm_medium=readme&utm_campaign=graph-theory) has a quiz on road transportation and lessons on transportation management, free and in the browser.
- **100+ case studies with their source code:** [samirsaci.com](https://www.samirsaci.com/?utm_source=github&utm_medium=readme&utm_campaign=graph-theory)

## About me

Samir Saci, supply chain engineer and data scientist with ten years in operations across Asia and Europe. Founder of [LogiGreen](https://www.logi-green.com/), creator of [Supply Science](https://www.youtube.com/@SupplyScience).
For consulting on analytics and sustainable supply chain transformation: [LogiGreen](https://www.logi-green.com/). More about me: [samirsaci.com/about](https://www.samirsaci.com/about/) · [LinkedIn](https://www.linkedin.com/in/samir-saci/)

