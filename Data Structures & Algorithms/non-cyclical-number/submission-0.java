class Solution {
    public boolean isHappy(int n) {
        Set<Integer> myset = new HashSet<>();

        while (n != 1) {
            String str = String.valueOf(n);
            n = 0;
            for (char s : str.toCharArray()) {
                int digit = Character.getNumericValue(s);
                n = n + digit * digit;
            }
            if (myset.contains(n)){
                return false;
            }
            myset.add(n);
        }
        return true;
    }
}
