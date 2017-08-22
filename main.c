#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int T;
	int i;
  int temp;
  int _mod_, x,y;
  double n_mod;
  double d_n, d_m;
  int n,m;
	// Number of tests
	scanf("%d",&T);

	for(i=0; i < T; i++)
    {
        scanf("%d %d", &n, &m);

        // If n is completely divisible by m(not equal to 0), then output n only.
        if(n % m == 0)
        {
            printf("%d\n",n);

        } else {

            // Find number closest to n and divisible by m
            _mod_ = n % m;

            // printf("MOD: %d\n",_mod_);
            d_n = n;
            d_m = m;
            n_mod = d_n / d_m;

            x = round(n_mod)*m;
            temp = x;

            // Result
            printf("%d\n",temp);
        }
    }

	return 0;
}
