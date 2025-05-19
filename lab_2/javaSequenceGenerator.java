import java.util.Random;

public class javaSequenceGenerator {

    public static String generateRandomBinaryString(int length) {
        Random randomGenerator = new Random(); 

        StringBuilder sequenceBuilder = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            sequenceBuilder.append(randomGenerator.nextInt(2));
        }
        return sequenceBuilder.toString();
    }

    public static void main(String[] args) {
        final int DesiredSequenceLength = 128;
        String binaryOutput = generateRandomBinaryString(DesiredSequenceLength);

        System.out.println("My generated Java sequence (" + DesiredSequenceLength + " bits):");
        System.out.println(binaryOutput);
    }
}