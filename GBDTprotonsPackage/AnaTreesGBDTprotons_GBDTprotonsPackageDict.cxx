// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME AnaTreesGBDTprotons_GBDTprotonsPackageDict

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "AnaTreeTools.h"
#include "MyLArTools.h"
#include "PandoraNuTrack.h"
#include "calcAnaTree.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *calcAnaTree_Dictionary();
   static void calcAnaTree_TClassManip(TClass*);
   static void *new_calcAnaTree(void *p = 0);
   static void *newArray_calcAnaTree(Long_t size, void *p);
   static void delete_calcAnaTree(void *p);
   static void deleteArray_calcAnaTree(void *p);
   static void destruct_calcAnaTree(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::calcAnaTree*)
   {
      ::calcAnaTree *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::calcAnaTree));
      static ::ROOT::TGenericClassInfo 
         instance("calcAnaTree", "calcAnaTree.h", 30,
                  typeid(::calcAnaTree), DefineBehavior(ptr, ptr),
                  &calcAnaTree_Dictionary, isa_proxy, 4,
                  sizeof(::calcAnaTree) );
      instance.SetNew(&new_calcAnaTree);
      instance.SetNewArray(&newArray_calcAnaTree);
      instance.SetDelete(&delete_calcAnaTree);
      instance.SetDeleteArray(&deleteArray_calcAnaTree);
      instance.SetDestructor(&destruct_calcAnaTree);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::calcAnaTree*)
   {
      return GenerateInitInstanceLocal((::calcAnaTree*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::calcAnaTree*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *calcAnaTree_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::calcAnaTree*)0x0)->GetClass();
      calcAnaTree_TClassManip(theClass);
   return theClass;
   }

   static void calcAnaTree_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *box_Dictionary();
   static void box_TClassManip(TClass*);
   static void *new_box(void *p = 0);
   static void *newArray_box(Long_t size, void *p);
   static void delete_box(void *p);
   static void deleteArray_box(void *p);
   static void destruct_box(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::box*)
   {
      ::box *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::box));
      static ::ROOT::TGenericClassInfo 
         instance("box", "PandoraNuTrack.h", 31,
                  typeid(::box), DefineBehavior(ptr, ptr),
                  &box_Dictionary, isa_proxy, 4,
                  sizeof(::box) );
      instance.SetNew(&new_box);
      instance.SetNewArray(&newArray_box);
      instance.SetDelete(&delete_box);
      instance.SetDeleteArray(&deleteArray_box);
      instance.SetDestructor(&destruct_box);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::box*)
   {
      return GenerateInitInstanceLocal((::box*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::box*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *box_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::box*)0x0)->GetClass();
      box_TClassManip(theClass);
   return theClass;
   }

   static void box_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *PandoraNuTrack_Dictionary();
   static void PandoraNuTrack_TClassManip(TClass*);
   static void *new_PandoraNuTrack(void *p = 0);
   static void *newArray_PandoraNuTrack(Long_t size, void *p);
   static void delete_PandoraNuTrack(void *p);
   static void deleteArray_PandoraNuTrack(void *p);
   static void destruct_PandoraNuTrack(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::PandoraNuTrack*)
   {
      ::PandoraNuTrack *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::PandoraNuTrack));
      static ::ROOT::TGenericClassInfo 
         instance("PandoraNuTrack", "PandoraNuTrack.h", 68,
                  typeid(::PandoraNuTrack), DefineBehavior(ptr, ptr),
                  &PandoraNuTrack_Dictionary, isa_proxy, 4,
                  sizeof(::PandoraNuTrack) );
      instance.SetNew(&new_PandoraNuTrack);
      instance.SetNewArray(&newArray_PandoraNuTrack);
      instance.SetDelete(&delete_PandoraNuTrack);
      instance.SetDeleteArray(&deleteArray_PandoraNuTrack);
      instance.SetDestructor(&destruct_PandoraNuTrack);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::PandoraNuTrack*)
   {
      return GenerateInitInstanceLocal((::PandoraNuTrack*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::PandoraNuTrack*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *PandoraNuTrack_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::PandoraNuTrack*)0x0)->GetClass();
      PandoraNuTrack_TClassManip(theClass);
   return theClass;
   }

   static void PandoraNuTrack_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *AnaTreeTools_Dictionary();
   static void AnaTreeTools_TClassManip(TClass*);
   static void *new_AnaTreeTools(void *p = 0);
   static void *newArray_AnaTreeTools(Long_t size, void *p);
   static void delete_AnaTreeTools(void *p);
   static void deleteArray_AnaTreeTools(void *p);
   static void destruct_AnaTreeTools(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::AnaTreeTools*)
   {
      ::AnaTreeTools *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::AnaTreeTools));
      static ::ROOT::TGenericClassInfo 
         instance("AnaTreeTools", "AnaTreeTools.h", 51,
                  typeid(::AnaTreeTools), DefineBehavior(ptr, ptr),
                  &AnaTreeTools_Dictionary, isa_proxy, 4,
                  sizeof(::AnaTreeTools) );
      instance.SetNew(&new_AnaTreeTools);
      instance.SetNewArray(&newArray_AnaTreeTools);
      instance.SetDelete(&delete_AnaTreeTools);
      instance.SetDeleteArray(&deleteArray_AnaTreeTools);
      instance.SetDestructor(&destruct_AnaTreeTools);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::AnaTreeTools*)
   {
      return GenerateInitInstanceLocal((::AnaTreeTools*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::AnaTreeTools*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *AnaTreeTools_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::AnaTreeTools*)0x0)->GetClass();
      AnaTreeTools_TClassManip(theClass);
   return theClass;
   }

   static void AnaTreeTools_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_calcAnaTree(void *p) {
      return  p ? new(p) ::calcAnaTree : new ::calcAnaTree;
   }
   static void *newArray_calcAnaTree(Long_t nElements, void *p) {
      return p ? new(p) ::calcAnaTree[nElements] : new ::calcAnaTree[nElements];
   }
   // Wrapper around operator delete
   static void delete_calcAnaTree(void *p) {
      delete ((::calcAnaTree*)p);
   }
   static void deleteArray_calcAnaTree(void *p) {
      delete [] ((::calcAnaTree*)p);
   }
   static void destruct_calcAnaTree(void *p) {
      typedef ::calcAnaTree current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::calcAnaTree

namespace ROOT {
   // Wrappers around operator new
   static void *new_box(void *p) {
      return  p ? new(p) ::box : new ::box;
   }
   static void *newArray_box(Long_t nElements, void *p) {
      return p ? new(p) ::box[nElements] : new ::box[nElements];
   }
   // Wrapper around operator delete
   static void delete_box(void *p) {
      delete ((::box*)p);
   }
   static void deleteArray_box(void *p) {
      delete [] ((::box*)p);
   }
   static void destruct_box(void *p) {
      typedef ::box current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::box

namespace ROOT {
   // Wrappers around operator new
   static void *new_PandoraNuTrack(void *p) {
      return  p ? new(p) ::PandoraNuTrack : new ::PandoraNuTrack;
   }
   static void *newArray_PandoraNuTrack(Long_t nElements, void *p) {
      return p ? new(p) ::PandoraNuTrack[nElements] : new ::PandoraNuTrack[nElements];
   }
   // Wrapper around operator delete
   static void delete_PandoraNuTrack(void *p) {
      delete ((::PandoraNuTrack*)p);
   }
   static void deleteArray_PandoraNuTrack(void *p) {
      delete [] ((::PandoraNuTrack*)p);
   }
   static void destruct_PandoraNuTrack(void *p) {
      typedef ::PandoraNuTrack current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::PandoraNuTrack

namespace ROOT {
   // Wrappers around operator new
   static void *new_AnaTreeTools(void *p) {
      return  p ? new(p) ::AnaTreeTools : new ::AnaTreeTools;
   }
   static void *newArray_AnaTreeTools(Long_t nElements, void *p) {
      return p ? new(p) ::AnaTreeTools[nElements] : new ::AnaTreeTools[nElements];
   }
   // Wrapper around operator delete
   static void delete_AnaTreeTools(void *p) {
      delete ((::AnaTreeTools*)p);
   }
   static void deleteArray_AnaTreeTools(void *p) {
      delete [] ((::AnaTreeTools*)p);
   }
   static void destruct_AnaTreeTools(void *p) {
      typedef ::AnaTreeTools current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::AnaTreeTools

namespace ROOT {
   static TClass *vectorlEintgR_Dictionary();
   static void vectorlEintgR_TClassManip(TClass*);
   static void *new_vectorlEintgR(void *p = 0);
   static void *newArray_vectorlEintgR(Long_t size, void *p);
   static void delete_vectorlEintgR(void *p);
   static void deleteArray_vectorlEintgR(void *p);
   static void destruct_vectorlEintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<int>*)
   {
      vector<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<int>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<int>", -2, "vector", 457,
                  typeid(vector<int>), DefineBehavior(ptr, ptr),
                  &vectorlEintgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<int>) );
      instance.SetNew(&new_vectorlEintgR);
      instance.SetNewArray(&newArray_vectorlEintgR);
      instance.SetDelete(&delete_vectorlEintgR);
      instance.SetDeleteArray(&deleteArray_vectorlEintgR);
      instance.SetDestructor(&destruct_vectorlEintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<int>*)0x0)->GetClass();
      vectorlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEintgR(void *p) {
      return  p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<int> : new vector<int>;
   }
   static void *newArray_vectorlEintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<int>[nElements] : new vector<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEintgR(void *p) {
      delete ((vector<int>*)p);
   }
   static void deleteArray_vectorlEintgR(void *p) {
      delete [] ((vector<int>*)p);
   }
   static void destruct_vectorlEintgR(void *p) {
      typedef vector<int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<int>

namespace ROOT {
   static TClass *vectorlEfloatgR_Dictionary();
   static void vectorlEfloatgR_TClassManip(TClass*);
   static void *new_vectorlEfloatgR(void *p = 0);
   static void *newArray_vectorlEfloatgR(Long_t size, void *p);
   static void delete_vectorlEfloatgR(void *p);
   static void deleteArray_vectorlEfloatgR(void *p);
   static void destruct_vectorlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<float>*)
   {
      vector<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<float>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<float>", -2, "vector", 457,
                  typeid(vector<float>), DefineBehavior(ptr, ptr),
                  &vectorlEfloatgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<float>) );
      instance.SetNew(&new_vectorlEfloatgR);
      instance.SetNewArray(&newArray_vectorlEfloatgR);
      instance.SetDelete(&delete_vectorlEfloatgR);
      instance.SetDeleteArray(&deleteArray_vectorlEfloatgR);
      instance.SetDestructor(&destruct_vectorlEfloatgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<float> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<float>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<float>*)0x0)->GetClass();
      vectorlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEfloatgR(void *p) {
      return  p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<float> : new vector<float>;
   }
   static void *newArray_vectorlEfloatgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<float>[nElements] : new vector<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEfloatgR(void *p) {
      delete ((vector<float>*)p);
   }
   static void deleteArray_vectorlEfloatgR(void *p) {
      delete [] ((vector<float>*)p);
   }
   static void destruct_vectorlEfloatgR(void *p) {
      typedef vector<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<float>

namespace ROOT {
   static TClass *vectorlEPandoraNuTrackgR_Dictionary();
   static void vectorlEPandoraNuTrackgR_TClassManip(TClass*);
   static void *new_vectorlEPandoraNuTrackgR(void *p = 0);
   static void *newArray_vectorlEPandoraNuTrackgR(Long_t size, void *p);
   static void delete_vectorlEPandoraNuTrackgR(void *p);
   static void deleteArray_vectorlEPandoraNuTrackgR(void *p);
   static void destruct_vectorlEPandoraNuTrackgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<PandoraNuTrack>*)
   {
      vector<PandoraNuTrack> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<PandoraNuTrack>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<PandoraNuTrack>", -2, "vector", 457,
                  typeid(vector<PandoraNuTrack>), DefineBehavior(ptr, ptr),
                  &vectorlEPandoraNuTrackgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<PandoraNuTrack>) );
      instance.SetNew(&new_vectorlEPandoraNuTrackgR);
      instance.SetNewArray(&newArray_vectorlEPandoraNuTrackgR);
      instance.SetDelete(&delete_vectorlEPandoraNuTrackgR);
      instance.SetDeleteArray(&deleteArray_vectorlEPandoraNuTrackgR);
      instance.SetDestructor(&destruct_vectorlEPandoraNuTrackgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<PandoraNuTrack> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<PandoraNuTrack>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEPandoraNuTrackgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<PandoraNuTrack>*)0x0)->GetClass();
      vectorlEPandoraNuTrackgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEPandoraNuTrackgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEPandoraNuTrackgR(void *p) {
      return  p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<PandoraNuTrack> : new vector<PandoraNuTrack>;
   }
   static void *newArray_vectorlEPandoraNuTrackgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::TOperatorNewHelper*)p) vector<PandoraNuTrack>[nElements] : new vector<PandoraNuTrack>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEPandoraNuTrackgR(void *p) {
      delete ((vector<PandoraNuTrack>*)p);
   }
   static void deleteArray_vectorlEPandoraNuTrackgR(void *p) {
      delete [] ((vector<PandoraNuTrack>*)p);
   }
   static void destruct_vectorlEPandoraNuTrackgR(void *p) {
      typedef vector<PandoraNuTrack> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<PandoraNuTrack>

namespace {
  void TriggerDictionaryInitialization_libAnaTreesGBDTprotons_GBDTprotonsPackage_Impl() {
    static const char* headers[] = {
"AnaTreeTools.h",
"MyLArTools.h",
"PandoraNuTrack.h",
"calcAnaTree.h",
0
    };
    static const char* includePaths[] = {
"/Users/erezcohen/larlite/UserDev/mySoftware",
"/Users/erezcohen/larlite/UserDev/MyLarLite/MyPackage",
"/Users/erezcohen/larlite/UserDev/BasicTool/GeoAlgo",
"/Users/erezcohen/larlite/core",
"/Users/erezcohen/root6/root-6.04.10/include",
"/Users/erezcohen/larlite/UserDev/AnaTreesGBDTprotons/GBDTprotonsPackage/",
0
    };
    static const char* fwdDeclCode = 
R"DICTFWDDCLS(
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$calcAnaTree.h")))  calcAnaTree;
struct __attribute__((annotate("$clingAutoload$PandoraNuTrack.h")))  box;
class __attribute__((annotate("$clingAutoload$PandoraNuTrack.h")))  PandoraNuTrack;
class __attribute__((annotate("$clingAutoload$AnaTreeTools.h")))  AnaTreeTools;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "AnaTreeTools.h"
#include "MyLArTools.h"
#include "PandoraNuTrack.h"
#include "calcAnaTree.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"AnaTreeTools", payloadCode, "@",
"PandoraNuTrack", payloadCode, "@",
"box", payloadCode, "@",
"calcAnaTree", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("libAnaTreesGBDTprotons_GBDTprotonsPackage",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_libAnaTreesGBDTprotons_GBDTprotonsPackage_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_libAnaTreesGBDTprotons_GBDTprotonsPackage_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_libAnaTreesGBDTprotons_GBDTprotonsPackage() {
  TriggerDictionaryInitialization_libAnaTreesGBDTprotons_GBDTprotonsPackage_Impl();
}
