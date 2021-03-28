package onnx_test;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtSession;
import ai.onnxruntime.OrtUtil;

import java.util.HashMap;

public class iris_more_flowers {
    public static void main (String[] args){
        try{
            OrtEnvironment environment = OrtEnvironment.getEnvironment();
            OrtSession session = environment.createSession(
                    "c:\\vs\\programovani\\python\\workshopy\\repozitar\\machine_learning\\iris_onnx.onnx",
                    new OrtSession.SessionOptions()
            );

            float[] moreFlowersInputData = {
                    6.1f, 2.8f, 4.7f, 1.2f,
                    5.7f, 3.8f, 1.7f, 0.3f,
                    7.7f, 2.6f, 6.9f, 2.3f
            };
            long[] moreFlowersInputShape = {3,4};
            Object moreFlowersReshaped = OrtUtil.reshape(moreFlowersInputData, moreFlowersInputShape);
            OnnxTensor moreFlowersTensor = OnnxTensor.createTensor(environment, moreFlowersReshaped);

            HashMap<String, OnnxTensor> inputData = new HashMap<>();
            inputData.put("float_input",moreFlowersTensor);

            OrtSession.Result results = session.run(inputData);
            long[] resultsArray = ((long[])results.get(0).getValue());
            for (long oneResult:resultsArray){
                System.out.println("Predicted class: " + oneResult);
            }
            System.out.println("Predicted probabilities: " + results.get(1).getValue());
        }catch(Exception e){
            System.out.println("Following error has occurred:");
            System.out.println(e);
        }
    }
}
