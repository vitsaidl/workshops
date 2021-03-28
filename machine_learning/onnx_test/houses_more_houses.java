package onnx_test;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtSession;
import ai.onnxruntime.OrtUtil;

import java.util.HashMap;

public class houses_more_houses {
    public static void main(String[] args){
        try{
            OrtEnvironment environment = OrtEnvironment.getEnvironment();
            OrtSession session = environment.createSession(
                    "c:\\vs\\programovani\\python\\workshopy\\repozitar\\machine_learning\\houses_onnx.onnx",
                    new OrtSession.SessionOptions()
            );

            HashMap<String, OnnxTensor> inputData = new HashMap<>();
            long[] housesInputShape = {3,1};

            String[] dataMSSubClass = {"20", "60", "30"};
            OnnxTensor tensorMSSubClassData = OnnxTensor.createTensor(
                    environment, dataMSSubClass, housesInputShape
            );
            inputData.put("MSSubClass",tensorMSSubClassData);

            String[] dataMSZoningData = {"RL", "RL", "RM"};
            OnnxTensor tensorMSZoning = OnnxTensor.createTensor(
                    environment, dataMSZoningData, housesInputShape
            );
            inputData.put("MSZoning",tensorMSZoning);

            float[] dataLotFrontage = {70.0f, 98.0f, 56.0f};
            Object reshapedLotFrontage = OrtUtil.reshape(dataLotFrontage, housesInputShape);
            OnnxTensor tensorLotFrontage = OnnxTensor.createTensor(environment, reshapedLotFrontage);
            inputData.put("LotFrontage",tensorLotFrontage);

            float[] dataLotArea = {8414.0f, 12256.0f, 8960.0f};
            Object reshapedLotArea = OrtUtil.reshape(dataLotArea, housesInputShape);
            OnnxTensor tensorLotArea = OnnxTensor.createTensor(environment, reshapedLotArea);
            inputData.put("LotArea",tensorLotArea);

            OrtSession.Result results = session.run(inputData);
            float[][] resultsArray = (float[][])results.get(0).getValue();
            for (float[] oneResult:resultsArray){
                System.out.println(oneResult[0]);
            }
        }catch (Exception e){
            System.out.println("Following error has occurred:");
            System.out.println(e);
        }
    }
}
