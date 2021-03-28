package onnx_test;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtSession;
import ai.onnxruntime.OrtUtil;

import java.util.HashMap;

public class iris_one_flower {

    public static void main(String[] args){
        try{
            OrtEnvironment environment = OrtEnvironment.getEnvironment();
            OrtSession session = environment.createSession(
                    "c:\\vs\\programovani\\python\\workshopy\\repozitar\\machine_learning\\iris_onnx.onnx",
                    new OrtSession.SessionOptions()
            );

            float[] oneFlowerInputData = {6.1f, 2.8f, 4.7f, 1.2f};
            long[] oneFlowerInputShape = {1,4};
            Object oneFlowerReshaped = OrtUtil.reshape(oneFlowerInputData, oneFlowerInputShape);
            OnnxTensor oneFlowerTensor = OnnxTensor.createTensor(environment, oneFlowerReshaped);

            HashMap<String, OnnxTensor> inputData = new HashMap<>();
            inputData.put("float_input",oneFlowerTensor);

            OrtSession.Result results = session.run(inputData);
            System.out.println("Predicted class: " + ((long[])results.get(0).getValue())[0]);
            System.out.println("Predicted probability: " + results.get(1).getValue());
        }catch(Exception e){
            System.out.println("Following error has occurred:");
            System.out.println(e);
        }
    }
}
