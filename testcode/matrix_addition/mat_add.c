void mat_add(int mat1[], int mat2[], int mat3[], int n)
{
	for(int i=0; i<n; ++i)
		mat3[i] = mat1[i] + mat2[i];
}

int main()
{
	
	// matrices are 1-d because they're continguous in memory
	// it could be called an array sum, but whatever
	int mat1[] = {1, -1, 256, -256, 65536, -65536};
	int mat2[] = {10, 176, 3072, 53248, 917504, 15728640};
	int mat3[] = {0, 0, 0, 0, 0, 0};
	mat_add(mat1, mat2, mat3, 6);
}
