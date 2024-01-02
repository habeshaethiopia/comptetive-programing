class Solution {
    public void moveZeroes(int[] nums) {
        int l,r,t;
        l=0;r=0;
        if (nums.length==1||nums.length==0)
        return;
        for(;r<nums.length;)
        { if (nums[r]==0)
           r++;
        else
           {t=nums[l];
            nums[l]=nums[r];
            nums[r]=t;
            r++;
            l++;} }
      
    }

}