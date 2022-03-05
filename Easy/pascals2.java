package Easy;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> first_row = new ArrayList<>();
        first_row.add(1);
        result.add(first_row);
        
        for(int i = 1; i <= rowIndex; i++){
            List<Integer> prev_row = result.get(i - 1);
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for(int j = 1; j < i; j++){
                row.add(prev_row.get(j - 1) + prev_row.get(j));
            }
            row.add(1);
            result.add(row);
        }
        return result.get(rowIndex);
    }
}
