// void search(Node root) {
//     if(node == null) return;

//     // 1. root 노드 방문
//     visit(root);
//     root.visited = true; // 1-1. 방문 노드 표시

//     // 2. root 노드와 인접한 정점 모두 방문
//     for each(Node n in root.adjacent) {
//         if(n.visited == false) { // 4. 방문하지 않은 정점 찾기
//             search(n); // 3. root 노드와 인접한 정점을 시작으로 DFS를 시작
//         }
//     }
// }
