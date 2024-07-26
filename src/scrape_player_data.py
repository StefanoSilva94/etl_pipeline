# def scrape_data_from_table_columns(soup: BeautifulSoup, cols_dict: dict, table_attribute_dict: dict,
#                                    table_index: int = 0) -> pd.DataFrame:
#     """
#     Scrapes data from a specified table in an HTML document and returns it as a pandas DataFrame.
#
#     :param soup: BeautifulSoup object to scrape data from
#     :param cols_dict: Dictionary where keys are column names and values are booleans indicating if the column contains href links
#     :param table_attribute_dict: Dictionary of attributes used to identify the HTML table (e.g., {'class': 'my-table'})
#     :param table_index: Index of the table to scrape data from (default is 0 for the first table)
#     :return: pd.DataFrame containing the scraped data
#     """
#     # Find all tables matching the attributes
#     tables = soup.find_all("table", **table_attribute_dict)
#
#     # Initialize data dictionary
#     data_dict = {col: [] for col in cols_dict.keys()}
#
#     # Check if the desired table index is valid
#     if tables and 0 <= table_index < len(tables):
#         table = tables[table_index]
#         rows = table.find_all("tr")[1:]  # Skip header row
#
#         for row in rows:
#             for col, is_href in cols_dict.items():
#                 # Try to find data in <td> or <th> elements
#                 row_element = row.find("td", {"data-stat": col}) or row.find("th", {"data-stat": col})
#
#                 if row_element:
#                     if is_href:
#                         # Extract href link if present
#                         link = row_element.find("a", href=True)
#                         value = link["href"] if link else None
#                     else:
#                         # Extract text and strip any extra whitespace
#                         value = row_element.get_text(strip=True)
#                 else:
#                     value = None
#
#                 data_dict[col].append(value)
#
#     return pd.DataFrame(data_dict)



def scrape_player_data():
    pass


if __name__ == '__main__':
    scrape_player_data()
