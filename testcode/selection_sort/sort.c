#include "stdio.h"

void selection_sort(int ary[], int N)
{
	int ind_min, _min, temp;
	for(int i=0; i<N-1; ++i)
	{
		_min = ary[i];
		ind_min = i;
		for(int j=i+1; j<N; ++j)
		{
			if (ary[j] < _min)
			{
				_min = ary[j];
				ind_min = j;
			}
		}
		temp = ary[i];
		ary[i] = _min;
		ary[ind_min] = temp;
	}
}


int main(int argc, char** argv) {
	int ary[] = {1, -256, 16, -16777216, 4096, -1};
	selection_sort(ary, 6);
	for(int i=0; i<6; ++i)
	{
		printf("%i\n", ary[i]);
	}
}

