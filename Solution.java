class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(!list.contains(nums[i])){
                list.add(nums[i]);
            }
        }

        for(int i = 0; i < list.size(); i++){
            nums[i] = list.get(i);
        }
        return(list.size());
    }
}
