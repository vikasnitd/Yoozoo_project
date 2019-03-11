#include<bits/stdc++.h>
using namespace std;

int cost_matrix1[44][44] , cost_matrix2[44][44];

int mark[44][44];

void reset( int n ) {

  for( int i = 0; i < n; i++){
    
    for( int j = 0; j < n; j++){

      mark[i][j] = 0;

    }

  }

}

void step11( int n ) {

  for(int i = 0; i < n; i++){

    int mini = 1e9;

    for(int j = 0; j < n; j++){

      mini = min( mini , cost_matrix1[i][j]);

    }

    for(int j = 0; j < n; j++){
 
      cost_matrix1[i][j] -= mini;

    }

  }

}

void step12( int n ) {

  for(int i = 0; i < n; i++){

    int mini = 1e9;

    for(int j = 0; j < n; j++){

      mini = min( mini , cost_matrix1[j][i]);

    }

    for(int j = 0; j < n; j++){
 
      cost_matrix1[j][i] -= mini;

    }

  }

}


void row_and_col_red( int n ) {
 
  step11( n );
  step12( n );
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      cost_matrix2[i][j] = cost_matrix1[i][j];
    }
  }

}

void row_scanning( int n ){

  for(int i = 0; i < n; i++){

    int zero = 0;
    for(int j = 0; j < n; j++){

      if(cost_matrix2[i][j] == 0){
        zero++;
      }

    }
    if(zero == 1){

      for( int j = 0; j < n; j++){
        if(cost_matrix2[i][j] == 0){
          mark[i][j] = 1;
          for(int k = 0; k < n; k++){
              cost_matrix2[k][j] = -1;
          }
          break;
        }
      }

    }


  }

}

void col_scanning( int n ){

  for(int i = 0; i < n; i++){

    int zero = 0;
    for(int j = 0; j < n; j++){

      if(cost_matrix2[j][i] == 0){
        zero++;
      }

    }
    if(zero == 1){

      for( int j = 0; j < n; j++){
        if(cost_matrix2[j][i] == 0){
          mark[j][i] = 1;
          for(int k = 0; k < n; k++){
            if(cost_matrix2[j][k] == -1)
              cost_matrix2[j][k] = -2;
            else
              cost_matrix2[j][k] = -1;
          }
          break;
        }
      }

    }


  }

}

void step21( int n ) {

  row_scanning( n );

  col_scanning( n );

}
int step22( int n ) {

  int cnt = 0;

  for(int i = 0; i < n; i++){

    for(int j = 0; j < n; j++){

      if(mark[i][j]){
        cnt++;
      }

    }
  }

  return cnt;

}

void step23( int n ) {

  int mini = 1e9;

  for(int i = 0; i < n; i++){
    for(int j = 0; j <n; j++){
      if(cost_matrix2[i][j]>0){
        mini = min( mini , cost_matrix2[i][j]);
      }
    }
  }
  for(int i = 0; i < n; i++){
    for(int j = 0; j <n; j++){
      if(cost_matrix2[i][j] == -2){
        cost_matrix1[i][j] += mini;
      }else if(cost_matrix2[i][j] != -1){
        cost_matrix1[i][j] -= mini;
      }
    }
  }
  for(int i = 0; i < n; i++){
    for(int j = 0; j <n; j++){
        cost_matrix2[i][j] = cost_matrix1[i][j];
    }
  }


}

void optimation( int n ) {
  
  while(1){

    step21( n );

    if(step22( n ) == n){
      return ;
    }else{
      step23( n );
      reset( n );
    }

  }

}



int main(){ 
   #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    cin>>n;

    int cost_matrix[n+1][n+1];

    for(int i = 0;i<n;i++){
      for(int j=0;j<n;j++){
        cin>>cost_matrix[i][j];

        cost_matrix1[i][j] = cost_matrix[i][j];

      }
    }

    row_and_col_red( n );

    optimation( n );

    int total_cost = 0;

    for( int i = 0; i < n; i++){

      for( int j = 0; j < n; j++){

        if( mark[i][j] ){

          cout<<"Salesman number "<<(i+1)<<" should be sent to city number: "<<j+1<<"\n";

          total_cost += cost_matrix[i][j];

        }

      }

    }

    cout<<"Total cost of fare: "<<total_cost;

    
    return 0;
}