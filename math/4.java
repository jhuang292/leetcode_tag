class Solution {
	    public String longestPalindrome(String s) {
		            if (s == null || s.length() < 1) {
				                return "";
						        }
			            
			            int start = 0;
				            int end = 0;
					            for (int i = 0; i < s.length(); i++) {
							                int l1 = expand(s, i, i);
									            int l2 = expand(s, i, i+1);
										                int tmp = Math.max(l1, l2);
												            if (tmp > end - start + 1) {
														                    start = i - (tmp - 1) / 2;
																                    end = i + tmp / 2;
																		                }
													            }
						            if (end == s.length() - 1)
								                return s.substring(start);
							            return s.substring(start, end + 1);
								        }
	        
	        private int expand(String s, int l, int r) {
			        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
					            l--;
						                r++;
								        }
				        return r - l - 1;
					    }
}
