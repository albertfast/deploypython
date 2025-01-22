import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class MarkovChains {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        int k = Integer.parseInt(firstMultipleInput[2]);

        /* This is the only place I wrote code except those places marked for us to write code and the four methods I created. */
        List<List<String>> game = new ArrayList<>();
        List<List<Double>> initalState = new ArrayList<>();
        initalState.add(new ArrayList<>(Collections.nCopies(n * m, 0d)));
        HashMap<List<Integer>, List<Integer>> tunnelIndexes = new HashMap<>();

        IntStream.range(0, n).forEach(nItr -> {
            try {
                String row = bufferedReader.readLine();

                // Write your code here
                List<String> rowList = new ArrayList<>(Arrays.asList(row.split("")));
                if (rowList.contains("A")) {
                    initalState.get(0).set(nItr * m + rowList.indexOf("A"), 1d);
                    rowList.set(rowList.indexOf("A"), "O");
                }
                game.add(rowList);

            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        IntStream.range(0, k).forEach(kItr -> {
            try {
                String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int i1 = Integer.parseInt(secondMultipleInput[0]);

                int j1 = Integer.parseInt(secondMultipleInput[1]);

                int i2 = Integer.parseInt(secondMultipleInput[2]);

                int j2 = Integer.parseInt(secondMultipleInput[3]);

                // Write your code here
                game.get(i1 - 1).set(j1 - 1, "T");
                game.get(i2 - 1).set(j2 - 1, "T");
                List<Integer> tunnelIndex1 = new ArrayList<>(Arrays.asList(i1 - 1, j1 - 1));
                List<Integer> tunnelIndex2 = new ArrayList<>(Arrays.asList(i2 - 1, j2 - 1));
                tunnelIndexes.put(tunnelIndex1, tunnelIndex2);
                tunnelIndexes.put(tunnelIndex2, tunnelIndex1);

            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        // Write your code here
        List<List<Double>> matrix = createMatrix(game, tunnelIndexes);
        System.out.printf("%.6f", markovChain(matrix, initalState));

        bufferedReader.close();
    }

   public static double markovChain(List<List<Double>> transitionMatrix, List<List<Double>> initialState) {
        List<Double> absorbingStates = transitionMatrix.remove(transitionMatrix.size() - 1);

        double[][] initialStateArray = convertListTo2DArray(initialState);
        double[][] transitionMatrixArray = convertListTo2DArray(transitionMatrix);
        
        double[][] resultState = initialStateArray;
        double change = 1;
        double convergenceThreshold = 1e-10;
        int maxIterations = initialState.get(0).size() * 25;

        for(int i = 0; i< maxIterations ; i++) {
           if (change < convergenceThreshold) {
               break;
           }
            double[][] nextState = multiplyMatrices(resultState, transitionMatrixArray);
             change = calculateDifference(resultState, nextState);
             resultState = nextState;
        }

        List<List<Double>> finalState = convertArrayToList(resultState);
        
        double chanceWinning = 0, chanceAbsorbing = 0;
        for (double index : absorbingStates) {
            if (index > 0) {
                chanceWinning += finalState.get(0).get((int) index);
                chanceAbsorbing += finalState.get(0).get((int) index);
            } else {
                chanceAbsorbing += finalState.get(0).get((int) -index);
            }
        }
        return chanceWinning / (chanceAbsorbing == 0 ? 1 : chanceAbsorbing);
    }

    public static List<List<Double>> createMatrix(List<List<String>> game, HashMap<List<Integer>, List<Integer>> tunnelIndexes) {
        int n = game.size(), m = game.get(0).size();
        List<List<Double>> matrix = new ArrayList<>();
        List<Double> absorbingStates = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                String cell = game.get(i).get(j);
                List<Double> rowVector = new ArrayList<>(Collections.nCopies(n * m, 0d));
                List<Integer> pathIndexes1D = new ArrayList<>();

                if (cell.equals("%")) {
                    rowVector.set(i * m + j, 1d);
                    absorbingStates.add((double) (i * m + j));
                } else
                if (cell.equals("*")) {
                    rowVector.set(i * m + j, 1d);
                    absorbingStates.add((double) -(i * m + j));
                } else
                if (!(cell.equals("#"))) {
                    if (j + 1 < m && !game.get(i).get(j + 1).equals("#")) {
                        if (game.get(i).get(j + 1).equals("T")) {
                            List<Integer> endOfTunnel = tunnelIndexes.get(Arrays.asList(i, j + 1));
                            pathIndexes1D.add(endOfTunnel.get(0) * m + endOfTunnel.get(1));
                        } else {
                            pathIndexes1D.add(i * m + j + 1);
                        }
                    }
                    if (j - 1 >= 0 && !game.get(i).get(j - 1).equals("#")) {
                        if (game.get(i).get(j - 1).equals("T")) {
                            List<Integer> endOfTunnel = tunnelIndexes.get(Arrays.asList(i, j - 1));
                            pathIndexes1D.add(endOfTunnel.get(0) * m + endOfTunnel.get(1));
                        } else {
                            pathIndexes1D.add(i * m + j - 1);
                        }
                    }
                    if (i + 1 < game.size() && !game.get(i + 1).get(j).equals("#")) {
                        if (game.get(i + 1).get(j).equals("T")) {
                            List<Integer> endOfTunnel = tunnelIndexes.get(Arrays.asList(i + 1, j));
                            pathIndexes1D.add(endOfTunnel.get(0) * m + endOfTunnel.get(1));
                        } else {
                            pathIndexes1D.add((i + 1) * m + j);
                        }
                    }
                    if (i - 1 >= 0 && !game.get(i - 1).get(j).equals("#")) {
                        if (game.get(i - 1).get(j).equals("T")) {
                            List<Integer> endOfTunnel = tunnelIndexes.get(Arrays.asList(i - 1, j));
                            pathIndexes1D.add(endOfTunnel.get(0) * m + endOfTunnel.get(1));
                        } else {
                            pathIndexes1D.add((i - 1) * m + j);
                        }
                    }
                    if (cell.equals("T") && pathIndexes1D.isEmpty()) {
                        rowVector.set(i * m + j, 1d);
                        absorbingStates.add((double) -(i * m + j));
                    }
                    for (int index : pathIndexes1D) {
                        rowVector.set(index, 1d / pathIndexes1D.size());
                    }
                }
                matrix.add(rowVector);
            }
        }
        matrix.add(absorbingStates);
        return matrix;
    }

    public static double[][] multiplyMatrices(double[][] firstMatrix, double[][] secondMatrix) {
        double[][] result = new double[firstMatrix.length][secondMatrix[0].length];
        for (int row = 0; row < result.length; row++) {
            for (int col = 0; col < result[row].length; col++) {
                result[row][col] = multiplyMatricesCell(firstMatrix, secondMatrix, row, col);
            }
        }
        return result;
    }

    public static double multiplyMatricesCell(double[][] firstMatrix, double[][] secondMatrix, int row, int col) {
        double cell = 0;
        for (int i = 0; i < secondMatrix.length; i++) {
            cell += firstMatrix[row][i] * secondMatrix[i][col];
        }
        return cell;
    }

    public static double[][] convertListTo2DArray(List<List<Double>> list2D) {
        int numRows = list2D.size();
        int numCols = list2D.get(0).size();

        double[][] array2D = new double[numRows][numCols];

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                array2D[i][j] = list2D.get(i).get(j);
            }
        }

        return array2D;
    }

    public static List<List<Double>> convertArrayToList(double[][] array2D) {
        List<List<Double>> list2D = new ArrayList<>();

        for (double[] row : array2D) {
            List<Double> rowList = new ArrayList<>();
            for (double value : row) {
                rowList.add(value);
            }
            list2D.add(rowList);
        }

        return list2D;
    }
     public static double calculateDifference(double[][] firstMatrix, double[][] secondMatrix) {
        double difference = 0;
        for (int row = 0; row < firstMatrix.length; row++) {
            for (int col = 0; col < firstMatrix[row].length; col++) {
                 difference += Math.abs(firstMatrix[row][col] - secondMatrix[row][col]);
            }
        }
    return difference;
    }
}