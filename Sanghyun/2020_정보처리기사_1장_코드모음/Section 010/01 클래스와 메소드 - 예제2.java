public class Test {
	static class AAclass {
		int i;
		int j;
	}

	public static void main(String[] args) {
		AAclass myVal = new AAclass();
		myVal.i = 10;
		myVal.j = 20;
		myVal = change(myVal);
		System.out.printf("i=%d, j=%d\n", myVal.i, myVal.j);
	}

	static AAclass change(AAclass myVal) { 
		int temp;
		temp = myVal.i; 
		myVal.i = myVal.j; 
		myVal.j = temp; 
		return myVal; 
	}
}