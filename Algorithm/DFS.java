import java.util.*;

class Graph {

    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        g.DFS(2);
        g.DFS();
    }


    private int V; // 노드의 개수
    private LinkedList<Integer> adj[]; // 인접 리스트

    /**
     * 생성자
     */
    Graph(int v) {
        V = v;
        adj = new LinkedList[v];
        for(int i=0; i<v; i++) {
            adj[i] = new LinkedList<>(); 
        }
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void DFSUtil(int v, boolean[] visited) {

        visited[v] = true;

        Iterator<Integer> i = adj[v].listIterator();
        while(i.hasNext()) {
            int n = i.next();

            if(!visited[n]) {
                DFSUtil(n, visited);
            }
        }
    }

    void DFS(int v) {
        boolean visited[] = new boolean[V];

        DFSUtil(v, visited);
    }
    
    void DFS() {

        // 노드의 방문 여부 판단(초깃값: false)
        boolean visited[] = new boolean[V];

        for(int i=0; i<V; ++i) {
            if(visited[i] == false) {
                DFSUtil(i, visited);
            }
        }
    }

    
}