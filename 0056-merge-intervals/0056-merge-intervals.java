class Solution {
    public int[][] merge(int[][] intervals) {
         if (intervals.length == 0) {
            return new int[0][];
        }
        
        List<int[]> merged = new ArrayList<>();
        int[] currentInterval = intervals[0];
        merged.add(currentInterval);

        for (int i = 1; i < intervals.length; i++) {
            int currentStart = currentInterval[0];
            int currentEnd = currentInterval[1];
            int nextStart = intervals[i][0];
            int nextEnd = intervals[i][1];

            if (currentEnd >= nextStart) {
                // Overlapping intervals, merge them
                currentInterval[1] = Math.max(currentEnd, nextEnd);
            } else {
                // Non-overlapping interval, add to list
                currentInterval = intervals[i];
                merged.add(currentInterval);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }
}