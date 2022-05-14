int abs_sum(int ary[], int n)
{
	int sum = 0;
	int elem;
	for(int i=0; i<n; ++i)
	{
		elem = ary[i];
		sum += elem > 0 ? elem : -elem;
	}
	return sum;
}

int main()
{
	int ary[] = {14, -12, 2816, -40960};
	abs_sum(ary, 4);
}
