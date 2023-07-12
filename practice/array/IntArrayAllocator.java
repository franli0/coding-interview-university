public class IntArrayAllocator {

    public static int[] allocate(int size) {
        int[] array;

        if (size <= 16) {
            array = new int[size];
        } else {
            int nextPowerOf2 = 1;
            while (nextPowerOf2 < size) {
                nextPowerOf2 *= 2;
            }
            array = new int[nextPowerOf2];
        }

        return array;
    }

    public static void main(String[] args) {
        int[] array = IntArrayAllocator.allocate(100);
        System.out.println(array.length);
    }
}