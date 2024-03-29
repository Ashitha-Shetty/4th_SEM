import java.util.Scanner;
public class Warshalls {
 private int V; 
 private boolean[][] tc;
 
 public void getTC(int[][] graph)
 
{
 this.V = graph.length;
 tc = new boolean[V][V];
 for (int i = 0; i < V; i++) 
 { 
 for (int j = 0; j < V; j++) 
 if (graph[i][j] != 0)
 tc[i][j] = true;
 tc[i][i] = true;
 
}
 for (int i = 0; i < V; i++) 
 
{
 for (int j = 0; j < V; j++) 
 
{
 if (tc[j][i]) 
 for (int k = 0; k < V; k++) 
 if (tc[j][i] && tc[i][k]) 
 tc[j][k] = true; 
 
}
 
}
 
}
 public void displayTC()
 
{
 System.out.println("\nTransitive closure :\n");
 System.out.print(" ");
 for (int v = 0; v < V; v++)
 System.out.print(" " + v );
 System.out.println();
 for (int v = 0; v < V; v++) 
 
{
 System.out.print(v +" ");
 for (int w = 0; w < V; w++) 
 
{
 if (tc[v][w]) 
 System.out.print(" 1 ");
 else 
 System.out.print(" 0 ");
 
}
 System.out.println();

 }
 } 
 public static void main (String[] args) 
 {
 Scanner sc = new Scanner(System.in);
 
 Warshalls w = new Warshalls();
 
 System.out.println("Enter number of vertices\n");
 int V = sc.nextInt();
 System.out.println("\nEnter matrix\n");
 int[][] graph = new int[V][V];
 for (int i = 0; i < V; i++)
 for (int j = 0; j < V; j++)
 graph[i][j] = sc.nextInt();
 w.getTC(graph);
 w.displayTC();
 }
}