from svgpathtools import parse_path

need_reverse = "M666.234 151.393C659.33 160.281 612.734 189.893 600.234 193.393C587.734 196.893 582.708 195.573 577.234 191.695C573.234 187.893 571.438 185.196 570.177 181.5C569.197 178.625 568.731 173.366 568.731 169.615C568.731 165.814 568.764 162.062 569.186 158.277C569.5 155.464 569.443 152.099 570.527 149.43C571.457 147.138 572.373 154.139 572.373 156.607C572.373 163.723 571.439 170.835 570.349 177.864C569.26 184.893 566.536 188.538 561.346 191.496C556.155 194.453 550.116 193.5 544.704 191.695C539.224 189.868 535.463 184.349 534.334 178.786C533.307 173.728 536.188 164.863 539.493 161.192C542.799 157.521 551.292 154.478 554.77 152.844C558.248 151.209 561.811 149.926 565.493 148.807C565.493 148.807 568.777 147.931 570.931 147.685C576.944 147 561.157 149.571 556.464 153.243C551.772 156.914 543.177 159.801 539.677 160.5C534.677 161.498 530.148 161.632 525.279 160.968C516.294 159.743 507.546 151.129 507.041 142.576C507.489 141.616 513.108 144.712 513.847 145.108C517.397 147.01 521.325 149.657 523.583 153.286C527.175 159.059 528.735 163.837 528.735 170.884C528.735 177.144 525.789 184.824 521.74 189.266C518.814 192.476 512.735 199.893 498.735 192.393C487.235 184.393 491.267 172.164 493.235 164.893C495.678 155.864 505.735 145.051 503.735 144.393C499.735 143.076 486.035 197.5 470.677 197.5C462.087 197.5 463.677 187.5 463.677 181C463.677 170.033 462.174 135.576 443.235 136.893C425.586 138.119 424.632 168.685 423.735 177.783C423.122 184 418.343 204 418.677 205.839C419.146 208.418 420.182 207.783 420.427 207C420.672 206.217 425.838 159.524 427.512 145.841C429.185 132.158 432.092 104.808 432.092 104.808C432.092 104.808 436.067 46.3749 436.735 45.3925C437.403 44.4101 415.177 174.469 415.177 174.469C415.177 174.469 412.677 194.5 399.177 205.5C388.746 214 378.177 208.932 375.677 207C368.055 201.11 366.464 186.566 364.78 177.957C362.582 166.725 360.293 158.111 347.681 152.402C338.677 148.327 333.177 148 330.677 149C328.177 150 328.677 151.5 331.02 152.402C337.177 154.774 352.03 151 362.713 139.25C366.332 135.269 368.327 127.277 369.853 122.276C374.578 106.786 378.001 90.7547 386.889 76.867C394.526 64.9347 410.792 63.9341 424.792 56.4341C427.792 54.8269 406.565 61.4381 403.292 62.4341C385.062 67.9826 360.469 100.5 355.823 109C329.589 157 329.207 192.873 287.694 240.5C275.395 254.61 283.178 273.757 300.177 271C328.912 266.34 332.024 180.5 333.177 165C333.867 155.728 335.177 146 336.156 141.379C337.135 136.758 347.586 96.1252 355.823 74.2364C360.518 61.7598 365.112 49.2299 368.35 36.2807C371.587 23.3315 339.677 96.0381 326.177 133.5C312.677 170.962 285.177 204.106 279.038 208.873C275.058 211.963 268.293 217.243 265.038 208.873C259.586 194.854 267.038 164.599 259.038 159.421C253.141 155.604 246.503 157.921 244.857 158.747C238.538 161.921 235.11 167.829 234.038 174.469C227.776 213.235 224.375 221.323 227.776 217.911C231.177 214.5 234.038 162.637 234.038 152.421C234.038 142.205 246.075 58.9431 246.538 51.4209C247.001 43.8987 227.776 130.921 227.776 130.921L206.538 217.911C205.402 221.57 201.916 223.02 201.916 218.102C201.916 205.395 206.369 180.568 196.763 170.962C182.4 156.599 177.344 225.354 177.009 227.358C175.308 237.566 177.181 177.663 177.868 174.779C177.868 159.443 173.684 180.077 172.524 183.844C169.424 193.921 166.043 203.75 161.55 213.235C150.584 236.386 117.692 249.371 107.826 218.675C105.359 211 105.726 187.184 105.726 187.184C105.726 187.184 107.139 149.845 108.208 131.265C110.555 90.468 119.992 52.1849 126.148 12.1735C126.847 7.62582 123.916 17.7523 123.857 17.899C117.771 33.116 110.896 48.0203 103.15 62.4628C85.1096 96.0975 63.7381 127.43 44.0815 160.083C38.2277 169.808 -8.1277 250.709 24.7101 248.543C55.6773 246.5 80.9109 229.957 102.677 208.873C134.334 178.21 159.879 132.995 181.304 93.667"
path = parse_path(need_reverse)



print(path.reversed().d())