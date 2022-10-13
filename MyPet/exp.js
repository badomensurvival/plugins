/*
 * This file is part of MyPet
 *
 * Copyright © 2011-2019 Keyle
 * MyPet is licensed under the GNU Lesser General Public License.
 *
 * MyPet is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * MyPet is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

//  #####################################
//  ###                               ###
//  ### MyPet Exp-System Level Script ###
//  ###         by Keyle              ###
//  ###       MC 1.3.1 script         ###
//  #####################################
//
//      Usable Fields for the "info" Object:
//          info.type
//          info.worldGroup
//

//  Level 2-16 cost 17 XP points each
//  Level 17-31 cost 3 more XP points than the previous
//  Level 32-∞ cost 7 more XP points than the previous

//   |------------------|
//   |  Return Methods  |
//   |------------------|

function getExpByLevel(level, petType, worldGroup) {
    var baseFactor = 10, expFactor = 6;
    var sumFactor = Array.from({ length: parseInt(level) }, (_, i) => i * expFactor * (parseInt((i + 1) / 10) + 1));
    var expTable = [];

    for (var i = 0; i < parseInt(level); i++) {
        expTable.push();
        if (i == 0) {
            expTable[i] = baseFactor + sumFactor[i];
        } else {
            expTable[i] = expTable[i - 1] + baseFactor + sumFactor[i];
        }
    }

    if (level == 0) {
        return 0;
    }

    return expTable[level - 1];
}
