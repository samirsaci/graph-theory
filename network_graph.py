"""
Network Graph Analysis for Transportation Planning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
import networkx as nx


LIST_STORES = ['NB4', 'NB5', 'NB3', 'ZS1', 'TZ2', 'TZ1', 'WH2', 'BB1', 'NJ2',
       'MAS', 'WH1', 'AQ1', 'NJ3', 'HZ1', 'JX1', 'YP1', 'YP2', 'JD1',
       'JD2', 'JS1', 'MH1', 'MH2', 'NH1', 'WGQ1', 'CS1', 'CS2', 'ZJG1',
       'CZ1', 'CZ2', 'CZ3', 'YZ1', 'ZJ1', 'DY1', 'DY2', 'WX3', 'NT1',
       'NT2', 'HM1', 'SZ1', 'SZ4', 'SZ2', 'KS1', 'SZ3', 'WX1', 'WX2',
       'WX4', 'SX1', 'NB6', 'WH3']


def load_data():
    """Load store and delivery data from Excel files."""
    df_city = pd.read_excel('data/store province.xlsx', index_col=0)
    df_plan = pd.read_excel('data/delivery records.xlsx', index_col=0)
    return df_city, df_plan


def create_sample_data():
    """Create sample data for demonstration."""
    np.random.seed(42)

    # Sample city data
    provinces = ['JIANGSU'] * 30 + ['ZHEJIANG'] * 10 + ['ANHUI'] * 5 + ['SHANGHAI'] * 4
    df_city = pd.DataFrame({
        'Code': LIST_STORES,
        'Province': provinces[:len(LIST_STORES)]
    })

    # Sample delivery plan
    dates = pd.date_range('2016-09-01', '2017-08-31', freq='D')
    data = []
    for date in dates[:500]:
        capacity = np.random.choice([3.5, 5.0, 8.0], p=[0.6, 0.3, 0.1])
        n_stores = np.random.randint(1, 4)
        stores = list(np.random.choice(LIST_STORES, n_stores, replace=False))
        data.append({
            'Month': f"{date.year}-{date.month}",
            'Year-Week': f"{date.year}-{date.isocalendar()[1]}",
            'Date': date,
            'Capacity(T)': capacity,
            'Total_tons(T)': np.random.uniform(1, capacity),
            'List_Code': str(stores)
        })
    df_plan = pd.DataFrame(data)
    return df_city, df_plan


def plot_routes_per_truck_size(df_plan):
    """Bar plot of routes per truck size by month."""
    df_count = pd.DataFrame(df_plan.groupby(['Capacity(T)', 'Month'])['Total_tons(T)'].count())
    df_count.columns = ['Routes']
    df_count = pd.pivot_table(df_count, index='Month', values='Routes', columns='Capacity(T)').fillna(0)

    ax = df_count.plot.bar(figsize=(10, 6), edgecolor='black', y=3.5, color='tab:blue', legend=True)
    df_count.plot.bar(edgecolor='black', y=5.0, color='tab:green', legend=True, ax=ax)
    df_count.plot.bar(edgecolor='black', y=8.0, color='tab:brown', legend=True, ax=ax)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Number of routes', fontsize=12)
    plt.title('Number of routes per truck size', fontsize=12)
    plt.tight_layout()
    plt.savefig('routes_per_truck_size.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: routes_per_truck_size.png")


def plot_deliveries_pie(df_an):
    """Pie chart of delivery routes per truck size."""
    my_circle = plt.Circle((0, 0), 0.8, color='white')
    df_an.groupby(['Size'])[['#Stores']].sum().plot.pie(figsize=(8, 8), y='#Stores', legend=False, pctdistance=0.7,
                                            autopct='%1.1f%%', labeldistance=1.05,
                                            wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
    plt.xlabel('Business Vertical')
    plt.title('{:,} delivery routes per truck size (T)'.format(len(df_an)))
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('deliveries_pie.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: deliveries_pie.png")


def plot_stores_per_route(df_an):
    """Bar chart of stores per route by truck type."""
    df_strou = pd.DataFrame(df_an.groupby(['Month', 'Size'])['#Stores'].mean())
    df_strou.columns = ['stores']
    df_strou.reset_index(inplace=True)
    df_strou = pd.pivot_table(df_strou, index='Month', values='stores', columns='Size').fillna(0)

    cols_available = [c for c in [3.5, 5.0, 8.0] if c in df_strou.columns]
    df_strou = df_strou[cols_available]
    df_strou.columns = [f'{c} T' for c in cols_available]

    ax = df_strou.plot.bar(figsize=(12, 6), edgecolor='black',
                           color=['tab:red', 'yellow', 'tab:blue'][:len(cols_available)], legend=True)
    plt.xlabel('(Month)', fontsize=12)
    plt.ylabel('(Deliveries/Route)', fontsize=12)
    plt.title('Number of Store Deliveries per Route for each Truck Type', fontsize=12)
    plt.ylim([1.5, 3])
    plt.tight_layout()
    plt.savefig('stores_per_route.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: stores_per_route.png")


def plot_network_graph(df_graph, df_city, dict_color, title, filename):
    """Create and save network graph."""
    fig, ax = plt.subplots(figsize=(10, 7))
    G = nx.Graph()
    for link in df_graph.index:
        G.add_edge(df_graph.iloc[link]['Source'], df_graph.iloc[link]['Target'])

    df_cat = df_city.set_index('Code')
    df_cat = df_cat.reindex(G.nodes())
    df_cat['Province'] = pd.Categorical(df_cat['Province'])

    nx.draw(G, with_labels=False, node_color=df_cat['Province'].map(dict_color),
            node_size=100, edgecolors='black', alpha=1,
            font_size=11, font_color='black', width=1, verticalalignment='top')
    plt.title(title, fontsize=12)
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")


def main():
    """Main function for network graph analysis."""
    # Load data
    try:
        df_city, df_plan = load_data()
        print("Data loaded from files.")
    except FileNotFoundError:
        print("Data files not found. Using sample data.")
        df_city, df_plan = create_sample_data()

    dict_prov = dict(zip(df_city['Code'], df_city['Province']))
    print(f"{len(df_city):,} cities")
    print(f"{len(df_plan):,} routes")

    # Plot routes per truck size
    plot_routes_per_truck_size(df_plan)

    # Analysis dataframe
    df_an = df_plan[['Month', 'Year-Week', 'Date', 'Capacity(T)', 'Total_tons(T)', 'List_Code']].copy()
    df_an.columns = ['Month', 'Year-Week', 'Date', 'Size', 'Tons', 'Stores']

    for store in LIST_STORES:
        df_an[store] = df_an['Stores'].apply(lambda t: store in t) * 1
    df_an['#Stores'] = df_an[LIST_STORES].sum(axis=1)
    print(f"{df_an['Month'].nunique()} Months")

    # Pie chart
    plot_deliveries_pie(df_an)

    # Stores per route
    plot_stores_per_route(df_an)

    # Create nodes
    L1 = [i for i in combinations(LIST_STORES, 2)]
    df_nodes = pd.DataFrame({'Pair': L1})
    df_nodes['Source'] = df_nodes['Pair'].apply(lambda t: t[0])
    df_nodes['Target'] = df_nodes['Pair'].apply(lambda t: t[1])
    df_nodes.drop(['Pair'], axis=1, inplace=True)
    print(f"{len(df_nodes):,} combinations")

    # Calculate deliveries (all sizes)
    df_del1 = df_nodes.copy()
    for m in df_an['Month'].unique():
        df_temp = df_an[df_an['Month'] == m]
        df_del1[m] = df_del1[['Source', 'Target']].apply(
            lambda t: (df_temp[t['Source']] * df_temp[t['Target']]).sum().sum() / 2, axis=1).astype(int)
    df_del1['Total'] = df_del1[df_an['Month'].unique()].sum(axis=1)
    print(f"{(df_del1['Total'] > 0).sum()}/{len(df_del1)} non zero")

    # Calculate deliveries by truck size
    df_del2 = df_nodes.copy()  # 3.5T
    df_del3 = df_nodes.copy()  # 5.0T
    df_del4 = df_nodes.copy()  # 8.0T

    for m in df_an['Month'].unique():
        for df_del, size in [(df_del2, 3.5), (df_del3, 5.0), (df_del4, 8.0)]:
            df_temp = df_an[(df_an['Month'] == m) & (df_an['Size'] == size)]
            df_del[m] = df_del[['Source', 'Target']].apply(
                lambda t: (df_temp[t['Source']] * df_temp[t['Target']]).sum().sum() / 2, axis=1).astype(int)

    for df_del in [df_del2, df_del3, df_del4]:
        df_del['Total'] = df_del[df_an['Month'].unique()].sum(axis=1)

    dict_color = dict(zip(['ZHEJIANG', 'ANHUI', 'JIANGSU', 'SHANGHAI'], ["black", "red", "lightgreen", "orange"]))

    # Network graph (Full scope - all sizes)
    df_graph = df_del1[df_del1['Total'] > 0].copy().reset_index()
    for dic, loc in zip([dict_prov], ['Province']):
        df_graph['Source ' + loc] = df_graph['Source'].map(dic)
        df_graph['Target ' + loc] = df_graph['Target'].map(dic)
    plot_network_graph(df_graph, df_city, dict_color, 'Full Scope - All Sizes', 'network_full_scope.png')

    # Network graph (3.5T)
    df_graph = df_del2[df_del2['Total'] > 0].copy().reset_index()
    for dic, loc in zip([dict_prov], ['Province']):
        df_graph['Source ' + loc] = df_graph['Source'].map(dic)
        df_graph['Target ' + loc] = df_graph['Target'].map(dic)
    plot_network_graph(df_graph, df_city, dict_color, '3.5T Trucks', 'network_3_5T.png')

    # Network graph for a specific month (all sizes)
    MTH = '2016-10'
    df_graph = df_del1[df_del1[MTH] > 0].copy().reset_index()
    for dic, loc in zip([dict_prov], ['Province']):
        df_graph['Source ' + loc] = df_graph['Source'].map(dic)
        df_graph['Target ' + loc] = df_graph['Target'].map(dic)
    if len(df_graph) > 0:
        plot_network_graph(df_graph, df_city, dict_color, f'{MTH} - All Sizes', f'network_{MTH}_all.png')

    print("\n" + "=" * 60)
    print("NETWORK GRAPH ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
