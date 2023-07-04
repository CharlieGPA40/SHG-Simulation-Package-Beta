class characterTable:

    def charTable(self):
        self.chr_data = [
            ['C$_1$', 'E'],
            ['A', '+1']], \
            [['S$_2$', 'E', 'i', 'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', 'R$_x$, R$_y$, R$_z$', 'x$^2$, y$^2$, z$^2$, xy, xz, yz', '-'],
             ['A$_u$', '+1', '-1', 'x, y, z', '-',
              'x$^3$, y$^3$, z$^3$, x$^2$y, x$^2$z, y$^2$x, y$^2$z, z$^2$x, z$^2$y, xyz']], \
            [['C$_2$', 'E', 'C$_2$', 'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', 'z,R$_z$', 'x$^2$,y$^2$,z$^2$,xy', 'z$^3$, xyz, y$^2$z, x$^2$z'],
             ['B', '+1', '-1', 'x, y, R$_x$, R$_z$', 'yz, xz', 'xz$^2$, yz$^2$, x$^2$y, xy$^2$, x$^3$, y$^3$']], \
            [['C$_3$', 'E', 'C$_3$', '(C$_3$)$^2$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', 'z,R$_z$', 'x$^2$ + y$^2$,z$^2$',
              'z$^3$, y(3x$^2$-y$^2$), x(x$^2$-3y$^2$), z(x$^2$+y$^2$)'],
             ['E', '+1', '+$\epsilon$', '+$\epsilon^*$', 'x+iy; R$_x$+iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]'],
             ['E', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy; R$_x$-iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]']
             ], \
            [['C$_{2h}$', 'E', 'C$_2$(z)', 'i', '$\sigma_h$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$, y$^2$, z$^2$,xy', '-'],
             ['B$_g$', '+1', '-1', '+1', '-1', 'R$_x$,R$_y$', 'xz,yz', '-'],
             ['A$_u$', '+1', '+1', '-1', '-1', 'z', '-', 'z$^3$,xyz,x$^2$z,y$^2$z'],
             ['B$_u$', '+1', '-1', '-1', '+1', 'x,y', '-', 'xz$^2$,yz$^2$,x$^2$y,xy$^2$,x$^3$,y$^3$']], \
            [['D$_2$', 'E', 'C$_2$(z)', 'C$_2$(y)', 'C$_2$(x)', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', '-', 'x$^2$, y$^2$, z$^2$', 'xyz'],
             ['B$_1$', '+1', '+1', '-1', '-1', 'z, R$_z$', 'xy', 'z$^3$, y$^2$z, x$^2$z'],
             ['B$_2$', '+1', '-1', '+1', '-1', 'y, R$_y$', 'xz', 'y$^3$, yz$^2$, x$^2$y'],
             ['B$_3$', '+1', '-1', '-1', '+1', 'x, R$_x$', 'yz', 'x$^3$, xz$^2$, xy$^2$']], \
            [['C$_{2v}$', 'E', 'C$_2$(z)', '$\sigma_v$(xz)', '$\sigma_v$(yz)', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', 'z', 'x$^2$, y$^2$, z$^2$', 'z$^3$,x$^2$z,y$^2$z'],
             ['A$_2$', '+1', '+1', '-1', '-1', 'R$_z$', 'xy', 'xyz'],
             ['B$_1$', '+1', '-1', '+1', '-1', 'x,R$_y$', 'xz', 'xz$^2$,x$^3$,xy$^2$'],
             ['B$_2$', '+1', '-1', '-1', '+1', 'y,R$_x$', 'yz', 'yz$^2$,y$^3$,x$^2$y']], \
            [['D$_{2h}$', 'E', 'C$_2$(z)', 'C$_2$(y)', 'C$_2$(x)', 'i', '$\sigma$(xy)', '$\sigma$(xz)', '$\sigma$(yz)',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$, y$^2$, z$^2$', '-'],
             ['B$_{1g}$', '+1', '+1', '-1', '-1', '+1', '+1', '-1', '-1', 'R$_z$', 'xy', '-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', 'R$_y$', 'xz', '-'],
             ['B$_{3g}$', '+1', '-1', '-1', '+1', '+1', '-1', '-1', '+1', 'R$_x$', 'yz', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-', '-', 'xyz'],
             ['B$_{1u}$', '+1', '+1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-', 'z$^3$,y$^2$z,x$^2$z'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', 'y', '-', 'yz$^2$,y$^3$,x$^2$y'],
             ['B$_{3u}$', '+1', '-1', '-1', '+1', '-1', '+1', '+1', '-1', 'x', '-', 'xz$^2$,xy$^2$,x$^3$']], \
            [['C$_4$', 'E', 'C$_4$', 'C$_2$', '(C$_4$)$^3$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', 'z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$, z(x$^2$+y$^2$)'],
             ['B', '+1', '-1', '+1', '-1', '-', 'x$^2$ - y$^2$,xy', 'xyz,z(x$^2$-y$^2$)'],
             ['E', '+1', '+i', '-1', '-i', 'x+iy; R$_x$+iR$_y$', '(yz,xz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E', '+1', '-i', '-1', '+i', 'x-iy; R$_x$-iR$_y$', '(yz,xz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['S$_4$', 'E', 'S$_4$', 'C$_2$', '(S$_4$)$^3$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$ + y$^2$,z$^2$', 'xyz,z(x$^2$-y$^2$)'],
             ['B', '+1', '-1', '+1', '-1', 'z', 'x$^2$ - y$^2$,xy', 'z$^3$,z(x$^2$+y$^2$)'],
             ['E', '+1', '+i', '-1', '-i', 'x+iy; R$_x$+iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E', '+1', '-i', '-1', '+i', 'x-iy; R$_x$-iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['C$_{4h}$', 'E', 'C$_4$(z)', 'C$_2$', '(C$_4$)$^3$', 'i', '(S$_4$)$^3$', '$\sigma_h$', 'S$_4$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$+y$^2$, z$^2$', '-'],
             ['B$_g$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', 'xy,x$^2$-y$^2$', '-'],
             ['E$_g$', '+1', '+i', '-1', '-i', '+1', '+i', '-1', '-i', 'R$_x$ +iR$_y$', '(xz,yz)', '-'],
             ['E$_g$', '+1', '-i', '-1', '+i', '+1', '-i', '-1', '+i', 'R$_x$ -iR$_y$', '(xz,yz)', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', 'z', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_u$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-', '-', 'xyz, z(x$^2$-y$^2$)'],
             ['E$_u$', '+1', '+i', '-1', '-i', '-1', '-i', '+1', '+i', 'x+iy', '-',
              '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E$_u$', '+1', '-i', '-1', '+i', '-1', '+i', '+1', '-i', 'x-iy', '-',
              '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['D$_4$', 'E', '2C$_4$(z)', 'C$_2$(z)', '2C$^\prime$$_2$', '2C$^{\prime\prime}$$_2$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', '-'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1', 'z,R$_z$', '-', 'z$^3$, z(x$^2$+y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '+1', '-1', '-', 'x$^2$-y$^2$', 'xyz'],
             ['B$_2$', '+1', '-1', '+1', '-1', '+1', '-', 'xy', 'z(x$^2$-y$^2$)'],
             ['E', '+2', '0', '-2', '0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)',
              '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['C$_{4v}$', 'E', '2C$_4$(z)', 'C$_2$', '2$\sigma_v$', '2$\sigma_d$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', 'z', 'x$^2$+y$^2$, z$^2$', 'z$^3$, z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_1$', '+1', '-1', '+1', '+1', '-1', '-', 'x$^2$-y$^2$', 'z(x$^2$-y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1', '+1', '-', 'xy', 'xyz'],
             ['E', '+2', '0', '-2', '0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)',
              '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['D$_{2d}$', 'E', '2S$_4$(z)', 'C$_2$(z)', '2C$^\prime_2$', '2$\sigma_d$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', 'xyz'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', 'z(x$^2$-y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '+1', '-1', '-', 'x$^2$-y$^2$', '-'],
             ['B$_2$', '+1', '-1', '+1', '-1', '+1', 'z', 'xy', 'z$^3$, z(x$^2$+y$^2$)'],
             ['E', '+2', '0', '-2', '0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)',
              '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['D$_{4h}$', 'E', '2C$_4$(z)', 'C$_2$', '2C$^\prime$$_2$', '2C$^{\prime\prime}$$_2$', 'i', '2S$_4$',
              '$\sigma_h$', '2$\sigma_v$', '2$\sigma_d$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', '-'],
             ['A$_{2g}$', '+1', '+1', '+1', '-1', '-1', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_{1g}$', '+1', '-1', '+1', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '-', 'x$^2$-y$^2$', '-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '+1', '-1', '+1', '-', 'xy', '-'],
             ['E$_g$', '+2', '0', '-2', '0', '0', '+2', '0', '-2', '0', '0', '(R$_x$,R$_y$)', '(xy,yz)', '-'],
             ['A$_{1u}$', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$_{2u}$', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_{1u}$', '+1', '-1', '+1', '+1', '-1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'xyz'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'z(x$^2$-y$^2$)'],
             ['E$_u$', '+2', '0', '-2', '0', '0', '-2', '0', '+2', '0', '0', '(x,y)', '-',
              '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']], \
            [['C$_3$', 'E', 'C$_3$', '(C$_3$)$^2$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', 'z,R$_z$', 'x$^2$ + y$^2$,z$^2$',
              'z$^3$,y(3x$^2$-y$^2$),x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['E', '+1', '+$\epsilon$', '+$\epsilon^*$', 'x+iy; R$_x$+iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]'],
             ['E', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy; R$_x$-iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]']], \
            [['S$_6$', 'E', 'C$_3$(z)', '(C$_3$)$^2$', 'i', '(S$_6$)$^2$', 'S$_6$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_{g}$', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_2$', 'x$^2$+y$^2$,z$^2$', '-'],
             ['E$_g$', '+1', '+$\epsilon$', '+$\epsilon^*$', '+1', '+$\epsilon$', '+$\epsilon^*$', 'R$_x$+iR$_y$',
              '(x$^2$-y$^2$,xy)(xz,yz)', '-'],
             ['E$_g$', '+1', '+$\epsilon^*$', '+$\epsilon$', '+1', '+$\epsilon^*$', '+$\epsilon$', 'R$_x$-iR$_y$',
              '(x$^2$-y$^2$,xy)(xz,yz)', '-'],
             ['A$_{u}$', '+1', '+1', '+1', '-1', '-1', '-1', 'z', '-',
              'z$^3$,y(3x$^2$-y$^2$),x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['E$_u$', '+1', '+$\epsilon$', '+$\epsilon^*$', '-1', '-$\epsilon$', '-$\epsilon^*$', 'x+iy', '-',
              '(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_u$', '+1', '+$\epsilon^*$', '+$\epsilon$', '-1', '-$\epsilon^*$', '-$\epsilon$', 'x-iy', '-',
              '(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']], \
            [['D$_3$', 'E', '2C$_3$(z)', '3C$^{\prime\prime}$$_v$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', 'x(x$^2$-3y$^2$)'],
             ['A$_2$', '+1', '+1', '-1', 'z,R$_z$', '-', 'z$^3$,y(3x$^2$-y$^2$),z(x$^2$+y$^2$)'],
             ['E', '+2', '-1', '0', '(x, y)(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)',
              '(xz$^2$, yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']], \
            [['C$_{3v}$', 'E', '2C$_3$(z)', '3$\sigma_v$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', 'z', 'x$^2$+y$^2$, z$^2$', 'z$^3$,x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '-1', 'R$_z$', '-', 'y(3x$^2$-y$^2$)'],
             ['E', '+2', '-1', '0', '(x, y)(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)',
              '(xz$^2$, yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']], \
            [['D$_{3d}$', 'E', '2C$_3$', '3C$^\prime$$_2$', 'i', '2S$_6$', '3$\sigma_d$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', '-'],
             ['A$_{2g}$', '+1', '+1', '-1', '+1', '+1', '-1', 'R$_z$', '-', '-'],
             ['E$_g$', '+2', '-1', '0', '+2', '-1', '0', '(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)', '-'],
             ['A$_{1u}$', '+1', '+1', '+1', '-1', '-1', '-1', '-', '-', 'x(x$^2$-3$y^2$)'],
             ['A$_{2u}$', '+1', '+1', '-1', '-1', '-1', '+1', 'z', '-', 'y(3x$^2$-y$^2$), z$^3$,z(x$^2$+y$^2$)'],
             ['E$_u$', '+2', '-1', '0', '-2', '+1', '0', '(x,y)', '-',
              '(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)']], \
            [['C$_6$', 'E', 'C$_6$', 'C$_3$', 'C$_2$', '(C$_3$)$^2$', '(C$_6$)$^5$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', '+1', '+1', 'z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'y(3x$^2$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$_1$', '+1', '+$\epsilon$', '-$\epsilon^*$', '-1', '-$\epsilon$', '+$\epsilon^*$', 'x+iy; R$_x$+iR$_y$',
              '(xz,yz)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_1$', '+1', '+$\epsilon^*$', '-$\epsilon$', '-1', '-$\epsilon^*$', '+$\epsilon$', 'x-iy; R$_x$-iR$_y$',
              '(xz,yz)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-', '(x$^2$-y$^2$,xy)',
              '[xyz,z(x$^2$-y$^2$]'],
             ['E$_2$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '-', '(x$^2$-y$^2$,xy)',
              '[xyz,z(x$^2$-y$^2$]']], \
            [['C$_{3h}$', 'E', 'C$_3$(z)', '(C$_3$)$^2$', '$\sigma_h$', 'S$_3$', '(S$_3$)$^5$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$^\prime$', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$+y$^2$,z$^2$',
              'y(3x$^3$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$^\prime$', '+1', '+$\epsilon$', '+$\epsilon^*$', '+1', '+$\epsilon$', '+$\epsilon^*$', 'x+iy',
              '(x$^2$-y$^2$,xy)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$^\prime$', '+1', '+$\epsilon^*$', '+$\epsilon$', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy',
              '(x$^2$-y$^2$,xy)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['A$^{\prime\prime}$', '+1', '+1', '+1', '-1', '-1', '-1', 'z', '-', 'zx$^3$,z(x$^2$+y$^2$)'],
             ['E$^{\prime\prime}$', '+1', '+$\epsilon$', '+$\epsilon^*$', '-1', '-$\epsilon$', '-$\epsilon^*$',
              'R$_x$+iR$_y$',
              '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]'],
             ['E$^{\prime\prime}$', '+1', '+$\epsilon^*$', '+$\epsilon$', '-1', '-$\epsilon^*$', '-$\epsilon$',
              'R$_x$-iR$_y$',
              '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]'],
             ], \
            [['C$_{6h}$', 'E', 'C$_6$(z)', 'C$_3$', 'C$_2$', '(C$_3$)$^2$', '(C$_6$)$^5$', 'i', '(S$_3$)$^5$',
              '(S$_6$)$^5$', '$\sigma_h$', 'S$_6$', 'S$_3$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_z$',
              'x$^2$+y$^2$, z$^2$', '-'],
             ['B$_g$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', '-'],
             ['E$_{1g}$', '+1', '+$\epsilon$', '-$\epsilon^*$', '-1', '-$\epsilon$', '+$\epsilon^*$', '+1',
              '+$\epsilon$', '-$\epsilon^*$', '-1', '-$\epsilon$', '+$\epsilon^*$', 'R$_x$ +iR$_y$', '(xz,yz)', '-'],
             ['E$_{1g}$', '+1', '+$\epsilon^*$', '-$\epsilon$', '-1', '-$\epsilon^*$', '+$\epsilon$', '+1',
              '+$\epsilon^*$', '-$\epsilon$', '-1', '-$\epsilon^*$', '+$\epsilon$', 'R$_x$-iR$_y$', '(xz,yz)', '-'],
             ['E$_{2g}$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1',
              '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['E$_{2g}$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1',
              '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '+$\epsilon^*$', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-1', 'z', '-',
              'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_u$', '+1', '-1', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-1', '+1', '-', '-',
              'y(3x$^2$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$_{1u}$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-1',
              '+$\epsilon^*$', '+$\epsilon$', '-1', '+$\epsilon^*$', '+$\epsilon$', '-', '-',
              '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_u$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '-1',
              '+$\epsilon$', '+$\epsilon^*$', '-1', '+$\epsilon$', '-$\epsilon^*$', '-', '-', '[(xyz,z(x$^2$-y$^2$)]']], \
            [['D$_6$', 'E', '2C$_6$(z)', '2C$_3$(z)', 'C$_2$(z)', '3C$^{\prime}$$_2$', '3C$^{\prime\prime}$$_2$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', '-'],
             ['A$_2$', '+1', '+1', '+1', '+1', '-1', '-1', 'z,R$_z$', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'x(x$^2$-3y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'y(3x$^2$-y$^2$)'],
             ['E$_1$', '+2', '+1', '-1', '-2', '0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)',
              '(xz$^2$, yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+2', '-1', '-1', '+2', '0', '0', '-', '(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['C$_{6v}$', 'E', '2C$_6$(z)', '2C$_3$(z)', 'C$_2$(z)', '3$\sigma$$_v$', '3$\sigma$$_d$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '+1', 'z', 'x$^2$+y$^2$, z$^2$', 'z$^3$,z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_1$', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'x(x$^2$-3y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'y(3x$^2$-y$^2$)'],
             ['E$_1$', '+2', '+1', '-1', '-2', '0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)',
              '(xz$^2$, yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+2', '-1', '-1', '+2', '0', '0', '-', '(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['D$_{3h}$', 'E', '2C$_3$(z)', '3C$^\prime$$2$', '$\sigma$$_h$(xy)', '2SC$_3$', '3$\sigma$$_v$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$^\prime$$_1$', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$', 'x(x$^2$-3y$^2$)'],
             ['A$^\prime$$_2$', '+1', '+1', '-1', '+1', '+1', '-1', 'R$_z$', '-', 'y(3x$^2$-y$^2$)'],
             ['E$^\prime$', '+2', '-1', '0', '+2', '-1', '0', '(x,y)', '(x$^2$-y$^2$,xy)',
              '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['A$^{\prime\prime}$$_1$', '+1', '+1', '+1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$^{\prime\prime}$$_2$', '+1', '+1', '-1', '-1', '-1', '+1', 'z', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['E$^{\prime\prime}$', '+2', '-1', '0', '-2', '+1', '0', '(R$_x$,R$_y$)', '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['D$_{6h}$', 'E', '2C$_6$(z)', '2C$_3$', '2C$_2$', '3C$^\prime$$_2$', '3C$^{\prime\prime}$$_2$', 'i', '2S$_3$',
              '2S$_6$', '$\sigma_h$(xy)', '3$\sigma_d$', '3$\sigma_v$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '', 'x$^2$+y$^2$, z$^2$',
              '-'],
             ['A$_{2g}$', '+1', '+1', '+1', '+1', '-1', '-1', '+1', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_{1g}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', '-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '-1', '+1', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', '-'],
             ['E$_{1g}$', '+2', '+1', '-1', '-2', '0', '0', '+2', '+1', '-1', '-2', '0', '0', '(R$_x$,R$_y$)', '(xz,yz)',
              '-'],
             ['E$_{2g}$', '+2', '-1', '-1', '+2', '0', '0', '+2', '-1', '-1', '+2', '0', '0', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['A$_{1u}$', '+1', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$_{2u}$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-',
              'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_{1u}$', '+1', '-1', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-1', '+1', '-', '-',
              'x(x$^2$-3y$^2$)'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '-', '-',
              'y(3x$^2$-y$^2$)'],
             ['E$_{1u}$', '+2', '+1', '-1', '-2', '0', '0', '-2', '-1', '+1', '+2', '0', '0', '(x,y)', '-',
              '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_{2u}$', '+2', '-1', '-1', '+2', '0', '0', '-2', '+1', '+1', '-2', '0', '0', '-', '-',
              '[xyz,z(x$^2$-y$^2$)]']
             ], \
            [['T', 'E', '4C$_3$', '4(C$_3$)$^2$', '3C$_2$', 'linear functions, rotations', 'quadratic functions',
              'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$+z$^2$', '-'],
             ['E', '+1', '+$\epsilon$', '+$\epsilon$$^*$', '+1', '-', '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
             ['E', '+1', '+$\epsilon$$^*$', '+$\epsilon$', '+1', '-', '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
             ['T', '+3', '0', '0', '-1', '(x,y,z)(R$_x$,R$_y$,R$_z$)', '(xy,xz,yz)',
              '(x$^3$,y$^3$,z$^3$)(xy$^2$,x$^2$z,yz$^2$)(xz$^2$,x$^2$y,y$^2$z)']], \
            [['T$_h$', 'E', '4C$_3$', '4(C$_3$)$^2$', '3C$_2$', 'i', '4(S$_6$)$^5$', '4S$_6$', '3$\sigma$$_h$',
              'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$+z$^2$', '-'],
             ['E$_g$', '+1', '+$\epsilon$', '+$\epsilon$$^*$', '+1', '+1', '+$\epsilon$', '+$\epsilon$$^*$', '+1', '-',
              '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
             ['E$_g$', '+1', '+$\epsilon$$^*$', '+$\epsilon$', '+1', '+1', '+$\epsilon$$^*$', '+$\epsilon$', '+1', '-',
              '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
             ['T$_g$', '+3', '0', '0', '-1', '+3', '0', '0', '-1', '(R$_x$,R$_y$,R$_z$)', '(xy,xz,yz)', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-', '-', 'xyz'],
             ['E$_u$', '+1', '+$\epsilon$', '+$\epsilon$$^*$', '+1', '-1', '-$\epsilon$', '-$\epsilon$$^*$', '-1', '-', '-',
              '-'],
             ['E$_u$', '+1', '+$\epsilon$$^*$', '+$\epsilon$', '+1', '-1', '-$\epsilon$$^*$', '-$\epsilon$', '-1', '-', '-',
              '-'],
             ['T$_u$', '+3', '0', '0', '-1', '-3', '0', '0', '+1', '(x,y,z)', '-',
              '(x$^3$,y$^3$,z$^3$)(xy$^2$,x$^2$z,yz$^2$)(xz$^2$,x$^2$y,y$^2$z)']], \
            [['O', 'E', '8C$_3$', '6C$\prime$$_2$', '6C$_4$', '3C$_2$=(C$_4$)$^2$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$+z$^2$', '-'],
             ['A$_2$', '+1', '+1', '-1', '-1', '+1', '-', '-', 'xyz'],
             ['E', '+2', '-1', '0', '0', '+2', '-', '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
             ['T$_1$', '+3', '0', '-1', '+1', '-1', '(x,y,z)(R$_x$,R$_y$,R$_z$)', '-',
              '(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]'],
             ['T$_2$', '+3', '0', '+1', '-1', '-1', '-', '(xy,xz,yz)', '[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]']], \
            [['T$_d$', 'E', '8C$_3$', '3C$_2$', '6S$_4$', '6$\sigma$$_d$', 'linear functions, rotations',
              'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$+z$^2$', 'xyz'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1', '-', '-', '-'],
             ['E', '+2', '-1', '+2', '0', '0', '-', '(2z$^2$-x$^2$-y$^2$,x$^2$-y$^2$)', '-'],
             ['T$_1$', '+3', '0', '-1', '+1', '-1', '(R$_x$,R$_y$,R$_z$)', '-',
              '[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]'],
             ['T$_2$', '+3', '0', '-1', '-1', '+1', '(x,y,z)', '(xy,xz,yz)',
              '(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]']], \
            [['O$_h$', 'E', '8C$_3$', '6C$_2$', '6C$_4$', '3C$_2$=(C$_4$)$^2$', 'i', '6S$_4$', '8S$_6$', '3$\sigma$$_h$',
              '6$\sigma$$_d$', 'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$+z$^2$', ','],
             ['A$_{2g}$', '+1', '+1', '-1', '-1', '+1', '+1', '-1', '+1', '+1', '-1', '-', '-', '-'],
             ['E$_g$', '+2', '-1', '0', '0', '+2', '+2', '0', '-1', '+2', '0', '-', '(2z$^2$-x$^2$-y$^2$,x$^2$-y$^2$)',
              '-'],
             ['T$_{1g}$', '+3', '0', '-1', '+1', '-1', '+3', '+1', '0', '-1', '-1', '(R$_x$,R$_y$,R$_z$)', '-', '-'],
             ['T$_{2g}$', '+3', '0', '+1', '-1', '-1', '+3', '-1', '0', '-1', '+1', '-', '(xz,yz,xy)', '-'],
             ['A$_{1u}$', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$_{2u}$', '+1', '+1', '-1', '-1', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'xyz'],
             ['E$_u$', '+2', '-1', '0', '0', '+2', '-2', '0', '+1', '-2', '0', '-', '-', '-'],
             ['T$_{1u}$', '+3', '0', '-1', '+1', '-1', '-3', '-1', '0', '+1', '+1', '(x,y,z)', '-',
              '(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]'],
             ['T$_{2u}$', '+3', '0', '+1', '-1', '-1', '-3', '+1', '0', '+1', '-1', '-', '-',
              '[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]']], \
            [['Iso', '1'],
             ['1', '1']]
        return self.chr_data