"""
pgm no 158
      *
     * *
    *   *
   *     *
  *       *
 *         *
* * * * * * * print the pattern
"""
print(' '*6+'*')
j=5
m=1
for i in range(5):
    print(' '*j+'*'+' '*m+'*')
    j-=1
    m+=2
print('* '*7)
