package com.aws.sample.rekognition.sdk;

import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.Image;
import software.amazon.awssdk.services.rekognition.model.DetectModerationLabelsRequest;
import software.amazon.awssdk.services.rekognition.model.DetectModerationLabelsResponse;
import software.amazon.awssdk.services.rekognition.model.ModerationLabel;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.List;

/**
 * To run this Java V2 code example, ensure that you have setup your development environment, including your credentials.
 * <p>
 * For information, see this documentation topic:
 * <p>
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DetectModerationLabelsSample {

    public static void main(String[] args) {

        final String USAGE = "\n" + "Usage: " + "   <sourceImage>\n\n" + "Where:\n" + "   sourceImage - the path to the image (for example, C:\\AWS\\pic1.png). \n\n";

        if (args.length < 1) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String sourceImage = args[0];
        Region region = Region.US_EAST_1;
        RekognitionClient rekClient = RekognitionClient.builder().region(region).build();

        detectModLabels(rekClient, sourceImage);
        rekClient.close();
    }

    public static void detectModLabels(RekognitionClient rekClient, String sourceImage) {

        try {
            InputStream sourceStream = new FileInputStream(sourceImage);
            SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);

            Image souImage = Image.builder().bytes(sourceBytes).build();

            DetectModerationLabelsRequest moderationLabelsRequest = DetectModerationLabelsRequest.builder().image(souImage).minConfidence(60F).build();

            long start = System.currentTimeMillis();

            DetectModerationLabelsResponse moderationLabelsResponse = rekClient.detectModerationLabels(moderationLabelsRequest);

            long end = System.currentTimeMillis();

            System.out.println("cost time:" + (end - start));

            // Display the results
            List<ModerationLabel> labels = moderationLabelsResponse.moderationLabels();
            System.out.println("Detected labels for image");

            for (ModerationLabel label : labels) {
                System.out.println("Label: " + label.name() + "\n Confidence: " + label.confidence().toString() + "%" + "\n Parent:" + label.parentName());
            }

        } catch (RekognitionException | FileNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}