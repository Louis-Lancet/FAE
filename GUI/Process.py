# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\Process.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Process(object):
    def setupUi(self, Process):
        Process.setObjectName("Process")
        Process.resize(1040, 822)
        self.gridLayout = QtWidgets.QGridLayout(Process)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Process)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.buttonLoadTrainingData = QtWidgets.QPushButton(self.groupBox)
        self.buttonLoadTrainingData.setObjectName("buttonLoadTrainingData")
        self.horizontalLayout_2.addWidget(self.buttonLoadTrainingData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lineEditTrainingData = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTrainingData.setObjectName("lineEditTrainingData")
        self.verticalLayout_3.addWidget(self.lineEditTrainingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.buttonLoadTestingData = QtWidgets.QPushButton(self.groupBox)
        self.buttonLoadTestingData.setObjectName("buttonLoadTestingData")
        self.horizontalLayout_3.addWidget(self.buttonLoadTestingData)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lineEditTestingData = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTestingData.setObjectName("lineEditTestingData")
        self.verticalLayout_4.addWidget(self.lineEditTestingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupNormalization = QtWidgets.QGroupBox(Process)
        self.groupNormalization.setObjectName("groupNormalization")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupNormalization)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkNormalizeUnit = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeUnit.setObjectName("checkNormalizeUnit")
        self.verticalLayout_7.addWidget(self.checkNormalizeUnit)
        self.checkNormalizeZeroCenter = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeZeroCenter.setObjectName("checkNormalizeZeroCenter")
        self.verticalLayout_7.addWidget(self.checkNormalizeZeroCenter)
        self.checkNormalizeUnitWithZeroCenter = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeUnitWithZeroCenter.setChecked(True)
        self.checkNormalizeUnitWithZeroCenter.setObjectName("checkNormalizeUnitWithZeroCenter")
        self.verticalLayout_7.addWidget(self.checkNormalizeUnitWithZeroCenter)
        self.checkNormalizationAll = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizationAll.setObjectName("checkNormalizationAll")
        self.verticalLayout_7.addWidget(self.checkNormalizationAll)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupNormalization)
        self.groupPreprocess = QtWidgets.QGroupBox(Process)
        self.groupPreprocess.setObjectName("groupPreprocess")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupPreprocess)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkRemoveSimilarFeatures = QtWidgets.QCheckBox(self.groupPreprocess)
        self.checkRemoveSimilarFeatures.setChecked(True)
        self.checkRemoveSimilarFeatures.setObjectName("checkRemoveSimilarFeatures")
        self.gridLayout_4.addWidget(self.checkRemoveSimilarFeatures, 1, 0, 1, 1)
        self.checkPCA = QtWidgets.QCheckBox(self.groupPreprocess)
        self.checkPCA.setObjectName("checkPCA")
        self.gridLayout_4.addWidget(self.checkPCA, 0, 0, 1, 1)
        self.checkPreprocessAll = QtWidgets.QCheckBox(self.groupPreprocess)
        self.checkPreprocessAll.setObjectName("checkPreprocessAll")
        self.gridLayout_4.addWidget(self.checkPreprocessAll, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupPreprocess)
        self.groupSelector = QtWidgets.QGroupBox(Process)
        self.groupSelector.setObjectName("groupSelector")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupSelector)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupSelector)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spinBoxMinFeatureNumber = QtWidgets.QSpinBox(self.groupSelector)
        self.spinBoxMinFeatureNumber.setMinimum(1)
        self.spinBoxMinFeatureNumber.setObjectName("spinBoxMinFeatureNumber")
        self.horizontalLayout_6.addWidget(self.spinBoxMinFeatureNumber)
        self.label_8 = QtWidgets.QLabel(self.groupSelector)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spinBoxMaxFeatureNumber = QtWidgets.QSpinBox(self.groupSelector)
        self.spinBoxMaxFeatureNumber.setMinimum(1)
        self.spinBoxMaxFeatureNumber.setProperty("value", 20)
        self.spinBoxMaxFeatureNumber.setObjectName("spinBoxMaxFeatureNumber")
        self.horizontalLayout_6.addWidget(self.spinBoxMaxFeatureNumber)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkANOVA = QtWidgets.QCheckBox(self.groupSelector)
        self.checkANOVA.setChecked(True)
        self.checkANOVA.setObjectName("checkANOVA")
        self.horizontalLayout_8.addWidget(self.checkANOVA)
        self.checkRFE = QtWidgets.QCheckBox(self.groupSelector)
        self.checkRFE.setObjectName("checkRFE")
        self.horizontalLayout_8.addWidget(self.checkRFE)
        self.checkRelief = QtWidgets.QCheckBox(self.groupSelector)
        self.checkRelief.setObjectName("checkRelief")
        self.horizontalLayout_8.addWidget(self.checkRelief)
        self.checkFeatureSelectorAll = QtWidgets.QCheckBox(self.groupSelector)
        self.checkFeatureSelectorAll.setObjectName("checkFeatureSelectorAll")
        self.horizontalLayout_8.addWidget(self.checkFeatureSelectorAll)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupSelector)
        self.groupClassifier = QtWidgets.QGroupBox(Process)
        self.groupClassifier.setObjectName("groupClassifier")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupClassifier)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkSVM = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkSVM.setChecked(True)
        self.checkSVM.setObjectName("checkSVM")
        self.gridLayout_5.addWidget(self.checkSVM, 0, 0, 1, 1)
        self.checkAE = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkAE.setObjectName("checkAE")
        self.gridLayout_5.addWidget(self.checkAE, 0, 1, 1, 1)
        self.checkRF = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkRF.setObjectName("checkRF")
        self.gridLayout_5.addWidget(self.checkRF, 2, 1, 1, 1)
        self.checkDecisionTree = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkDecisionTree.setObjectName("checkDecisionTree")
        self.gridLayout_5.addWidget(self.checkDecisionTree, 4, 1, 1, 1)
        self.checkLRLasso = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkLRLasso.setObjectName("checkLRLasso")
        self.gridLayout_5.addWidget(self.checkLRLasso, 3, 1, 1, 1)
        self.checkLDA = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkLDA.setObjectName("checkLDA")
        self.gridLayout_5.addWidget(self.checkLDA, 2, 0, 1, 1)
        self.checkNaiveBayes = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkNaiveBayes.setObjectName("checkNaiveBayes")
        self.gridLayout_5.addWidget(self.checkNaiveBayes, 5, 1, 1, 1)
        self.checkLogisticRegression = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkLogisticRegression.setObjectName("checkLogisticRegression")
        self.gridLayout_5.addWidget(self.checkLogisticRegression, 3, 0, 1, 1)
        self.checkGaussianProcess = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkGaussianProcess.setObjectName("checkGaussianProcess")
        self.gridLayout_5.addWidget(self.checkGaussianProcess, 5, 0, 1, 1)
        self.checkAdaboost = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkAdaboost.setObjectName("checkAdaboost")
        self.gridLayout_5.addWidget(self.checkAdaboost, 4, 0, 1, 1)
        self.checkClassifierAll = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkClassifierAll.setObjectName("checkClassifierAll")
        self.gridLayout_5.addWidget(self.checkClassifierAll, 6, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupClassifier)
        self.groupBox_2 = QtWidgets.QGroupBox(Process)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioLeaveOneOut = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioLeaveOneOut.setObjectName("radioLeaveOneOut")
        self.horizontalLayout_7.addWidget(self.radioLeaveOneOut)
        self.radio5folder = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio5folder.setChecked(True)
        self.radio5folder.setObjectName("radio5folder")
        self.horizontalLayout_7.addWidget(self.radio5folder)
        self.radio10Folder = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio10Folder.setObjectName("radio10Folder")
        self.horizontalLayout_7.addWidget(self.radio10Folder)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonRun = QtWidgets.QPushButton(Process)
        self.buttonRun.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonRun.setObjectName("buttonRun")
        self.verticalLayout.addWidget(self.buttonRun)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Process)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.listOnePipeline = QtWidgets.QListWidget(Process)
        self.listOnePipeline.setObjectName("listOnePipeline")
        self.verticalLayout_2.addWidget(self.listOnePipeline)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(Process)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.textEditDescription = QtWidgets.QTextEdit(Process)
        self.textEditDescription.setObjectName("textEditDescription")
        self.verticalLayout_6.addWidget(self.textEditDescription)
        self.line_2 = QtWidgets.QFrame(Process)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.label_4 = QtWidgets.QLabel(Process)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.textEditVerbose = QtWidgets.QTextEdit(Process)
        self.textEditVerbose.setObjectName("textEditVerbose")
        self.verticalLayout_6.addWidget(self.textEditVerbose)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Process)
        QtCore.QMetaObject.connectSlotsByName(Process)

    def retranslateUi(self, Process):
        _translate = QtCore.QCoreApplication.translate
        Process.setWindowTitle(_translate("Process", "Form"))
        self.groupBox.setTitle(_translate("Process", "Load"))
        self.label.setText(_translate("Process", "Training data"))
        self.buttonLoadTrainingData.setText(_translate("Process", "Load"))
        self.label_2.setText(_translate("Process", "Testing data"))
        self.buttonLoadTestingData.setText(_translate("Process", "Load"))
        self.groupNormalization.setTitle(_translate("Process", "Normalization"))
        self.checkNormalizeUnit.setText(_translate("Process", "Normalize to unit"))
        self.checkNormalizeZeroCenter.setText(_translate("Process", "Normalize to 0-center"))
        self.checkNormalizeUnitWithZeroCenter.setText(_translate("Process", "Normalize to unit with 0-center"))
        self.checkNormalizationAll.setText(_translate("Process", "All Normalization"))
        self.groupPreprocess.setTitle(_translate("Process", "Preprocess"))
        self.checkRemoveSimilarFeatures.setText(_translate("Process", "Remove Similar Features"))
        self.checkPCA.setText(_translate("Process", "PCA"))
        self.checkPreprocessAll.setText(_translate("Process", "All Preprocess"))
        self.groupSelector.setTitle(_translate("Process", "Feature Selector"))
        self.label_7.setText(_translate("Process", "minNumber"))
        self.label_8.setText(_translate("Process", "maxNumber"))
        self.checkANOVA.setText(_translate("Process", "ANOVA"))
        self.checkRFE.setText(_translate("Process", "RFE"))
        self.checkRelief.setText(_translate("Process", "Relief"))
        self.checkFeatureSelectorAll.setText(_translate("Process", "All Feature Selector"))
        self.groupClassifier.setTitle(_translate("Process", "Classifier"))
        self.checkSVM.setText(_translate("Process", "SVM"))
        self.checkAE.setText(_translate("Process", "AE"))
        self.checkRF.setText(_translate("Process", "Random Forest"))
        self.checkDecisionTree.setText(_translate("Process", "Decision Tree"))
        self.checkLRLasso.setText(_translate("Process", "LR-Lasso"))
        self.checkLDA.setText(_translate("Process", "LDA"))
        self.checkNaiveBayes.setText(_translate("Process", "Naive Bayes"))
        self.checkLogisticRegression.setText(_translate("Process", "Logistic Regression"))
        self.checkGaussianProcess.setText(_translate("Process", "Gaussian Process"))
        self.checkAdaboost.setText(_translate("Process", "Adaboost"))
        self.checkClassifierAll.setText(_translate("Process", "All Classifier"))
        self.groupBox_2.setTitle(_translate("Process", "Cross Validation"))
        self.radioLeaveOneOut.setText(_translate("Process", "LeaveOneOut"))
        self.radio5folder.setText(_translate("Process", "5-Folder"))
        self.radio10Folder.setText(_translate("Process", "10-Folder"))
        self.buttonRun.setText(_translate("Process", "Run and Save"))
        self.label_5.setText(_translate("Process", "Pipeline Description:"))
        self.label_3.setText(_translate("Process", "Data Description"))
        self.label_4.setText(_translate("Process", "Verbose"))

