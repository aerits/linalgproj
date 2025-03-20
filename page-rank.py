import numpy as np

class Page:
    name = "";
    links = [];
    def __init__(self, name: str, links: list[str]):
        self.name = name;
        self.links = links;

def page_rank(pages: list[Page], dampening: float) -> list[str]:
    arr = []
    page_indices = {}
    index = -1
    for page in pages:
        index += 1;
        page_indices[page.name] = index;
        # give each page an index
    for page in pages:
        # create a probability vector for each page
        page_arr = np.zeros(len(pages));
        page_arr[page_indices[page.name]] = 0
        for linked_page in page.links:
            page_arr[page_indices[linked_page]] += 1
        
        page_arr = page_arr + dampening
        total = sum(page_arr)
        page_arr = page_arr / total
        arr.append(page_arr)

    arr = np.matrix(arr);
    arr = arr.T;

    # create a steady state vector
    q = []
    for i in range(0, len(pages)):
        q.append([0])
    q = np.matrix(q)
    q[0,0] = 1;
    q = arr**1000 * q
    
    # create an array of (page name, page probability)
    new_array = []
    for i in range(0,len(pages)):
        new_array.append((pages[i].name, q[i,0]))
    
    # remove the highest page probability in new array and add to page ranking
    # do this until there are no more in new array
    page_ranking = []
    while len(new_array) > 0:
        maximum = (0, new_array[0][1]);
        for i in range(0,len(new_array)):
            if new_array[i][1] > maximum[1]:
                maximum = (i, new_array[i][1])
        page_ranking.append(new_array.pop(maximum[0])[0])
    return(page_ranking)
        
a = Page("A", ["B", "C"])
b = Page("B", [])
c = Page("C", ["B"])
pages = [a, b, c]
a = page_rank(pages, 0.12)
print(a)